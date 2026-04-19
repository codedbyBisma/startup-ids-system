from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://simple-ids-cloud-logs-default-rtdb.firebaseio.com"
})

app = Flask(__name__)

@app.route("/")
def dashboard():
    ref = db.reference("ids_logs")
    data = ref.get()

    alerts = []
    if data:
        for k, v in data.items():
            alerts.append(v)

    return render_template("dashboard.html", alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)
