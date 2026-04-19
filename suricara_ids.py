import json
import time
import os
from collections import Counter
from datetime import datetime

EVE_LOG = "/var/log/suricata/eve.json"

# Colors
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

alert_levels = Counter()
attacker_ips = Counter()
protocols = Counter()

print(f"{CYAN}🛡️  Suricata IDS Monitor Started (Live Alerts){RESET}\n")

def follow(file):
    file.seek(0, os.SEEK_END)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

try:
    with open(EVE_LOG, "r") as f:
        for line in follow(f):
            try:
                event = json.loads(line)

                if event.get("event_type") == "alert":
                    alert = event["alert"]
                    severity = alert.get("severity", 0)
                    signature = alert.get("signature", "Unknown")
                    src_ip = event.get("src_ip", "N/A")
                    proto = event.get("proto", "N/A")

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    if severity == 1:
                        color = RED
                        level = "HIGH"
                    elif severity == 2:
                        color = YELLOW
                        level = "MEDIUM"
                    else:
                        color = GREEN
                        level = "LOW"

                    print(f"{color}[{timestamp}] ALERT [{level}]")
                    print(f"   Attack : {signature}")
                    print(f"   Source : {src_ip}")
                    print(f"   Proto  : {proto}{RESET}\n")

                    alert_levels[level] += 1
                    attacker_ips[src_ip] += 1
                    protocols[proto] += 1

            except json.JSONDecodeError:
                continue

except KeyboardInterrupt:
    print(f"\n{CYAN}📊 IDS SUMMARY REPORT{RESET}")
    print("-" * 40)
    print("Alert Levels :", dict(alert_levels))
    print("Top Attackers:", attacker_ips.most_common(5))
    print("Protocols    :", dict(protocols))
    print(f"{RED}\n🛑 IDS Monitoring Stopped{RESET}")