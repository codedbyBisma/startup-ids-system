Cloud-Based Plug & Play Intrusion Detection System (IDS)

A lightweight, real-time Intrusion Detection System built for small businesses and startups. Monitors network traffic, detects threats, stores logs in the cloud, and displays alerts on a live web dashboard.

Project Overview

This IDS was built as a freelance security project for a startup client. It provides real-time threat detection, cloud-based log storage, and a simple web dashboard — designed to be easy to deploy with no advanced technical knowledge required.

Features

Real-time network monitoring using Suricata IDS engine

Live alerts with severity levels (HIGH / MEDIUM / LOW)

Cloud logging via Firebase Realtime Database

Web dashboard built with Flask to visualize alerts

Attack detection — port scans, brute force, suspicious connections

Tamper-proof logs with timestamps

Tech Stack

ComponentTechnologyDetection EngineSuricata IDSAlert MonitorPythonCloud StorageFirebase Realtime DatabaseDashboardFlask + HTML/CSSTesting EnvironmentKali LinuxAttack SimulationNmap

Project Structure

simple_ids/

├── suricata_ids.py       # Real-time alert monitor

├── cloud_logger.py       # Firebase cloud logging

├── app.py                # Flask dashboard backend

├── templates/

│   └── dashboard.html    # Frontend dashboard UI

└── README.md

Note: firebase_key.json is not included for security reasons. Add your own Firebase service account key to run the project.

How to Run

Step 1 — Install Suricata

sudo apt update

sudo apt install suricata -y

Step 2 — Start Suricata Monitoring

sudo suricata -c /etc/suricata/suricata.yaml -i eth0

Step 3 — Run Alert Monitor

sudo python3 suricata_ids.py

Step 4 — Send Logs to Firebase

pip install firebase-admin
python3 cloud_logger.py

Step 5 — Launch Dashboard

pip install flask firebase-admin

python3 app.py

Open browser: http://127.0.0.1:5000

Step 6 — Simulate Attack (Optional)

sudo nmap -sS <target_ip>

Screenshots
Phase 1:  Suricata engine running and live alerts.

![image alt](https://github.com/codedbyBisma/Startup-IDS-System/blob/ffa0357d57825ecc6d9b3507b98b5b99e20449f5/suricata%20code.png)

![image alt](https://github.com/codedbyBisma/Startup-IDS-System/blob/ad43ced1b2b1b266c67665c799594fbf7f275009/suricata%20test%20success.png)

![image alt](https://github.com/codedbyBisma/Startup-IDS-System/blob/ffa0357d57825ecc6d9b3507b98b5b99e20449f5/suricata%20starting.png)

![image alt](https://github.com/codedbyBisma/Startup-IDS-System/blob/ffa0357d57825ecc6d9b3507b98b5b99e20449f5/suricata%20script.png)

![image alt](https://github.com/codedbyBisma/Startup-IDS-System/blob/ffa0357d57825ecc6d9b3507b98b5b99e20449f5/summary%20of%20suricata%20script.png)

![image alt](https://github.com/codedbyBisma/Startup-IDS-System/blob/ffa0357d57825ecc6d9b3507b98b5b99e20449f5/nmap%20scan.png)


Phase 2: Logs sent to Firebase Cloud.
![image alt](https://github.com/codedbyBisma/Startup-IDS-System/blob/904d78a498f1b976763b17a330dafd2eae756a0b/output%20of%20firebase.png)

![image alt](https://github.com/codedbyBisma/Startup-IDS-System/blob/904d78a498f1b976763b17a330dafd2eae756a0b/logs%20sent%20to%20cloud.png)

Phase 3: Web dashboard displaying alerts

![image alt](https://github.com/codedbyBisma/Startup-IDS-System/blob/904d78a498f1b976763b17a330dafd2eae756a0b/dashboard.png)

Use Cases

Small business network monitoring

Startup security infrastructure

Learning intrusion detection concepts

Real-time threat observation

---

## Contributing

If you'd like to improve this IDS or add features (e.g., email alerts, GUI dashboard, more detection rules), feel free to fork the repo and send a pull request!

---

## License

This project is open source and available under the MIT License.

---

## Author

Developed by Bisma Khushi  

Cybersecurity Student & Freelance Security Developer  


