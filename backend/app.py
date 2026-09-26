from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DASHBOARD_DATA = {
    "route": "Ring Road, Jaipur",
    "session_id": 4,
    "hazards_found": 6,
    "km_covered": 3.4,
    "map50": 0.74,
    "severity_correlation": 0.63,
    "risk": "low",
    "gps_status": "GPS lock",
    "satellites": 12,

    "detections": [
        {
            "location": "MG Road, flyover",
            "severity": "high",
            "x": 140,
            "y": 401
        },
        {
            "location": "Sector 14 junction",
            "severity": "medium",
            "x": 330,
            "y": 276
        },
        {
            "location": "Tonk Road km 4.2",
            "severity": "high",
            "x": 470,
            "y": 156
        },
        {
            "location": "Civil Lines crossing",
            "severity": "low",
            "x": 600,
            "y": 96
        },
        {
            "location": "Ajmer Rd underpass",
            "severity": "medium",
            "x": 430,
            "y": 336
        },
        {
            "location": "Vidhyadhar Nagar",
            "severity": "high",
            "x": 650,
            "y": 426
        }
    ]
}


@app.route("/")
def home():
    return jsonify({
        "message": "PathSense Backend is Running!"
    })


@app.route("/api/status")
def status():
    return jsonify({
        "status": "active",
        "risk": DASHBOARD_DATA["risk"],
        "message": "PathSense system is working"
    })


@app.route("/api/dashboard")
def dashboard():
    return jsonify(DASHBOARD_DATA)


if __name__ == "__main__":
    app.run(debug=True)