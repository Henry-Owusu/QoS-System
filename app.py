import csv
from io import StringIO
import random
from flask import Flask, render_template, request, jsonify, make_response


app = Flask(__name__)

# Data for QoS settings. Don't forget to change in doc
qos_settings = {
    'voice': {'priority': 'high', 'bandwidth': '40%'},
    'video': {'priority': 'medium', 'bandwidth': '30%'},
    'data': {'priority': 'low', 'bandwidth': '30%'}
}

logs = [
    {"type": "Security", "message": "Unauthorized login attempt detected."},
    {"type": "System", "message": "System check completed successfully."},
    {"type": "Error", "message": "Database connection error."},
    {"type": "Update", "message": "System updated to version 1.2.3."},
    {"type": "User", "message": "New user account created."},
    {"type": "Warning", "message": "Low disk space warning."},
    {"type": "Network", "message": "Network latency issues detected."},
    {"type": "Performance", "message": "Performance metrics updated."},
    {"type": "Backup", "message": "Backup completed successfully."},
    {"type": "Maintenance", "message": "Scheduled maintenance starting."},
    {"type": "Security", "message": "Firewall rules updated."},
    {"type": "Error", "message": "Error processing user request."},
    {"type": "User", "message": "User profile updated."},
    {"type": "Warning", "message": "High CPU usage detected."},
    {"type": "System", "message": "Server reboot initiated."},
    {"type": "Update", "message": "New updates available."},
    {"type": "Performance", "message": "Performance optimization applied."}
]


def generate_mock_qos_data():
    return {
        'voice': {
            'bandwidth': f"{random.randint(50, 100)} Mbps",
            'latency': f"{random.randint(10, 40)} ms",
            'packet_loss': f"{random.random():.2f}%",
            'throughput': f"{random.randint(40, 80)} Mbps"
        },
        'data': {
            'bandwidth': f"{random.randint(100, 500)} Mbps",
            'latency': f"{random.randint(20, 70)} ms",
            'packet_loss': f"{random.random():.2f}%",
            'throughput': f"{random.randint(80, 200)} Mbps"
        },
        'video': {
            'bandwidth': f"{random.randint(200, 1000)} Mbps",
            'latency': f"{random.randint(10, 50)} ms",
            'packet_loss': f"{random.random():.2f}%",
            'throughput': f"{random.randint(150, 500)} Mbps"
        }
    }



@app.route('/')
def index():
    return render_template('index.html', qos_settings=qos_settings)


@app.route('/monitor_status')
def monitor_status():
    return render_template('monitor_status.html')



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', logs=logs)


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


@app.route('/policy')
def policy():
    return render_template('policy.html')


@app.route('/config')
def config():
    return render_template('config.html')



@app.route('/alerts')
def alerts():
    page = request.args.get('page', 1, type=int)
    logs_per_page = 10
    start = (page - 1) * logs_per_page
    end = start + logs_per_page
    total_pages = len(logs) // logs_per_page + (1 if len(logs) % logs_per_page else 0)
    return render_template('alerts.html', logs=logs[start:end], page=page, total_pages=total_pages)





@app.route('/export-logs')
def export_logs():
    
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Type', 'Message'])  # CSV header
    for log in logs:
        cw.writerow([log['type'], log['message']])
    
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=logs.csv"
    output.headers["Content-type"] = "text/csv"
    return output



@app.route('/api/network-stats')
def network_stats():
    stats = generate_mock_qos_data()
  
    return jsonify(stats)


@app.route('/update_qos', methods=['POST'])
def update_qos():
    category = request.form.get('category')
    priority = request.form.get('priority')
    bandwidth = request.form.get('bandwidth')

    if category in qos_settings:
        qos_settings[category]['priority'] = priority
        qos_settings[category]['bandwidth'] = bandwidth
        return jsonify({'message': 'QoS settings updated successfully!'})
    else:
        return jsonify({'message': 'Invalid category!'}), 400
    



if __name__ == '__main__':
    app.run(debug=True)