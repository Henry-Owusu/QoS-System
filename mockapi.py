from flask import Flask, jsonify
import random

app = Flask(__name__)

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

@app.route('/api/qos')
def qos():
    mock_data = generate_mock_qos_data()
    return jsonify(mock_data)

if __name__ == '__main__':
    app.run(debug=True)
