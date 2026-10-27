# IDS Setup and Testing Guide

## A. Prepare a safe lab
1. Create an Ubuntu VM in VirtualBox.
2. Prefer a Host-only or Internal Network adapter for isolated practice.
3. Record the VM's interface name and IP address. On Ubuntu, run `ip address`.
4. Update the VM and follow the official Snort installation guide for your Ubuntu version. Package names and setup steps vary by release; do not copy configuration paths blindly.

## B. Configure Snort
1. Check the installed version using `snort -V`.
2. Find the active Snort configuration and rules directory for that installation.
3. Back up the configuration before editing.
4. Add the rules from `local.rules` to the local rules file used by your configuration. Set `$HOME_NET` to the lab subnet in the configuration.
5. Test configuration syntax before running, using the option supported by your version (commonly `snort -T -c <config-path>`).
6. Start monitoring the authorized lab interface with the correct configuration and interface option for your Snort version. Check the installed version's help (`snort -h`) because Snort 2 and Snort 3 options differ.

## C. Validate alerts
- Generate a normal ping between two lab VMs you control and check whether the ICMP rule alerts.
- If testing SSH, connect only to the SSH service on your own lab VM and verify the alert is logged.
- Review the console output or configured alert log. Record timestamp, source, destination, rule message, and whether the alert was expected.
- Take your own screenshots of the successful rule test for the internship submission.

## D. Run the optional offline authentication detector
From this folder:
```bash
python auth_log_detector.py
```
Expected behavior: it flags the fictional `192.0.2.45` sample because it has at least five failed attempts. The `192.0.2.0/24` and `198.51.100.0/24` ranges are reserved for documentation examples.

To analyze an authorized log file:
```bash
python auth_log_detector.py /path/to/your/authorized/auth.log
```
The script only reads a text log and prints a summary; it does not block addresses or change the system.

## E. Response workflow
1. **Triage:** confirm which rule fired and inspect surrounding events.
2. **Scope:** identify source/destination assets and whether the traffic was expected.
3. **Preserve:** save relevant logs and timestamps according to your organization's process.
4. **Contain:** only take approved actions, such as a firewall change, after validation and authorization.
5. **Recover:** remediate exposed services, credentials, or misconfigurations.
6. **Document:** record evidence, false-positive assessment, actions, owner, and closure time.

## Evidence checklist for submission
- [ ] Snort version and lab interface documented
- [ ] Local rules included and syntax checked
- [ ] At least one alert observed in your own lab
- [ ] Screenshot of alert output
- [ ] False positives and limitations discussed
- [ ] Response workflow documented

## Limitations
The provided rules are basic examples. A SYN alert alone does not prove an attack, and this starter configuration is not a complete production IDS. Rule syntax and command-line flags can differ by Snort version.
