import firebase_admin
from firebase_admin import credentials, db
import json
import datetime

cred = credentials.Certificate("firebase_key.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://simple-ids-cloud-logs-default-rtdb.firebaseio.com/"
})

ref = db.reference("ids_logs")

with open("eve.json", "r", errors="ignore") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        try:
            data = json.loads(line)

            if data.get("event_type") == "alert":
                msg = data["alert"]["signature"]

                ref.push({
                    "type": "Suricata Alert",
                    "message": msg,
                    "timestamp": str(datetime.datetime.now())
                })

        except:
            continue

print("✅ Alerts sent to Firebase")
