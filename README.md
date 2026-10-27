# Task 4 — Network Intrusion Detection System (Snort)

## Objective
Set up a network-based IDS, detect suspicious traffic using rules, generate alerts, and document a response process.

## Recommended lab
Use an Ubuntu virtual machine and a host-only/internal VirtualBox network. Install Snort using the official instructions for your Ubuntu release. Interface names and package versions differ, so confirm them in your own VM.

## Files
- `local.rules` — example defensive Snort rules.
- `auth_log_detector.py` — optional offline detector for repeated failed SSH login events in an authorized lab log.
- `sample_auth.log` — fictional sample log for testing.
- `TESTING.md` — setup and validation procedure.

## Snort rule examples
The local rules alert on ICMP echo requests, TCP SYN packets directed at SSH, and repeated SSH connection attempts. They are starting points, not a replacement for tuning rules to your network and Snort version.

## Safety
Only monitor networks and systems you own or have explicit permission to monitor. Use a host-only lab for testing. Do not run intrusive scans against public IPs or third-party systems.

## Deliverables
1. A working IDS lab setup documented in `TESTING.md`.
2. Custom local rules in `local.rules`.
3. Alert validation notes and screenshots captured by you from your own lab.
4. Response steps: validate alert, identify source/destination, preserve logs, contain if authorized, investigate, and document closure.

## Note about response mechanisms
An IDS should not automatically block traffic unless that response has been explicitly designed, tested, and authorized. This project focuses on detection and documented response rather than risky automatic blocking.
