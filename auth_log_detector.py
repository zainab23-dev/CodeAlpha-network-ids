"""Offline, defensive detector for repeated SSH authentication failures in a log."""
import re
import sys
from collections import Counter
from pathlib import Path

FAILURE = re.compile(r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})")
THRESHOLD = 5

def detect(path: Path) -> int:
    if not path.is_file():
        print(f"Error: log file not found: {path}", file=sys.stderr)
        return 2
    counts = Counter()
    samples = {}
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line_no, line in enumerate(handle, start=1):
            match = FAILURE.search(line)
            if match:
                ip = match.group("ip")
                counts[ip] += 1
                samples.setdefault(ip, (match.group("user"), line_no))
    if not counts:
        print("No SSH failed-password events found in this file.")
        return 0
    print(f"Analyzed: {path}")
    print(f"Alert threshold: {THRESHOLD} failures per source IP in this file\n")
    alerts = 0
    for ip, count in counts.most_common():
        user, line_no = samples[ip]
        if count >= THRESHOLD:
            alerts += 1
            print(f"[ALERT] {ip}: {count} failed attempts; example user={user!r}, first matching line={line_no}")
        else:
            print(f"[INFO]  {ip}: {count} failed attempts")
    print(f"\nSummary: {alerts} source IP(s) met the threshold.")
    print("Investigate context before taking action; shared NATs and typos can create false positives.")
    return 0

if __name__ == "__main__":
    default = Path(__file__).with_name("sample_auth.log")
    chosen = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    raise SystemExit(detect(chosen))
