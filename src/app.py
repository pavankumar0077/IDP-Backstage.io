from flask import Flask, jsonify
import datetime
import socket
import os
import platform
import time
import psutil  # pip install psutil

app = Flask(__name__)
start_time = time.time()


@app.route('/api/v1/info')
def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great, little human! <3',
        'deployed_on': 'kubernetes'
    })


@app.route('/api/v1/healthz')
def health():
    # Do an actual check here
    return jsonify({'status': 'up'}), 200


@app.route('/api/v1/ip')
def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return jsonify({'ip_address': ip})


@app.route('/api/v1/uptime')
def get_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_string = str(datetime.timedelta(seconds=int(uptime_seconds)))
    return jsonify({'uptime': uptime_string})


@app.route('/api/v1/env')
def get_env():
    # Select only safe environment variables
    safe_env = {
        'USER': os.environ.get('USER', 'unknown'),
        'HOME': os.environ.get('HOME', 'unknown'),
        'SHELL': os.environ.get('SHELL', 'unknown'),
        'PYTHON_VERSION': platform.python_version(),
        'OS': platform.system()
    }
    return jsonify(safe_env)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
