from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

from scanner import run_port_scan, build_scan_presets
from learning_data import IMPORTANT_PORTS, PORT_CATEGORIES

app = Flask(__name__)
app.secret_key = "supersecretkey123"

SCAN_HISTORY = []

@app.route("/")
def home():
    presets = build_scan_presets()
    return render_template("index.html", presets=presets)

@app.route("/scan", methods=["POST"])
def scan():
    target = request.form.get("target", "").strip()
    scan_mode = request.form.get("scan_mode", "custom")
    custom_start = request.form.get("start_port", "").strip()
    custom_end = request.form.get("end_port", "").strip()
    timeout = request.form.get("timeout", "0.35").strip()

    if not target:
        flash("Please enter a target IP address or domain.", "error")
        return redirect(url_for("home"))

    try:
        timeout_value = float(timeout)
        if timeout_value <= 0 or timeout_value > 3:
            raise ValueError
    except ValueError:
        flash("Timeout must be between 0.1 and 3 seconds.", "error")
        return redirect(url_for("home"))

    presets = build_scan_presets()

    if scan_mode in presets:
        start_port, end_port = presets[scan_mode]["range"]
        preset_label = presets[scan_mode]["label"]
    else:
        try:
            start_port = int(custom_start)
            end_port = int(custom_end)
        except ValueError:
            flash("Custom start and end ports must be valid numbers.", "error")
            return redirect(url_for("home"))

        if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
            flash("Ports must be between 1 and 65535.", "error")
            return redirect(url_for("home"))

        if start_port > end_port:
            flash("Start port cannot be greater than end port.", "error")
            return redirect(url_for("home"))

        preset_label = "Custom Scan"

    scan_result = run_port_scan(
        target=target,
        start_port=start_port,
        end_port=end_port,
        timeout=timeout_value
    )

    history_item = {
        "target": scan_result["target_input"],
        "resolved_ip": scan_result["resolved_ip"],
        "start_port": start_port,
        "end_port": end_port,
        "scan_label": preset_label,
        "open_count": len(scan_result["open_ports"]),
        "closed_count": scan_result["closed_count"],
        "duration": scan_result["duration"],
        "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p")
    }

    SCAN_HISTORY.insert(0, history_item)
    if len(SCAN_HISTORY) > 20:
        SCAN_HISTORY.pop()

    return render_template(
        "results.html",
        result=scan_result,
        start_port=start_port,
        end_port=end_port,
        scan_label=preset_label
    )

@app.route("/learning")
def learning():
    return render_template(
        "learning.html",
        important_ports=IMPORTANT_PORTS,
        categories=PORT_CATEGORIES
    )

@app.route("/history")
def history():
    return render_template("history.html", history=SCAN_HISTORY)

@app.route("/about")
def about():
    presets = build_scan_presets()
    return render_template("history.html", history=SCAN_HISTORY, presets=presets, about_mode=True)

if __name__ == "__main__":
    app.run(debug=True)