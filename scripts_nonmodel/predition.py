from flask import Flask, request, jsonify
import json
import os
from prometheus_client import start_http_server, Summary, Gauge, Counter
import psutil
import sys

# Get the absolute path of the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path of the parent directory
parent_dir = os.path.join(current_dir, '..')

# Add the parent directory to sys.path
sys.path.insert(0, parent_dir)



from scripts_model import score


app = Flask(__name__)


# Create a metric to track time spent and requests made
# Create metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
CPU_USAGE = Gauge('cpu_usage_percent', 'CPU usage percentage')
MEMORY_USAGE = Gauge('memory_usage_percent', 'Memory usage percentage')
NETWORK_IO = Counter('network_io_bytes', 'Network I/O in bytes', ['direction'])




"""
# Load the python script and function
Use the import statement to load the script. If your script is named my_script.py, you can import it like this:
import my_script

Access Functions from the Script:
Once imported, you can access functions from my_script using dot notation. For example, if my_script has a function named my_function, you can call it as follows:
Python_function = my_script.my_function()
"""




@app.route("/ping", methods=["GET"])
def ping():
    """
    Health check endpoint.
    Returns 200 if the service is up.
    """
    return jsonify({"status": "ok"}), 200




@app.route("/invocations", methods=["POST"])
@REQUEST_TIME.time()
def invocations():
    """
    Endpoint for model inference.
    Expects JSON input and returns JSON output.
    """
    try:
        content_type = request.headers.get("Content-Type", "").lower()

        if content_type == "application/json":
            data = request.get_json()
            # Assuming score.run_xgboost expects a dictionary
            parsed_data = data
        else:
            raise ValueError(f"Unsupported Content-Type: {content_type}")

        r_result = score.run_xgboost(parsed_data)
        result = json.loads(list(r_result)[0])
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def collect_metrics():
    # Update CPU and memory usage
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().percent)

    # Update network I/O
    net_io = psutil.net_io_counters()
    NETWORK_IO.labels(direction='in').inc(net_io.bytes_recv)
    NETWORK_IO.labels(direction='out').inc(net_io.bytes_sent)


if __name__ == "__main__":
    # Start up the server to expose metrics
    start_http_server(8001)
    # Run the application
    app.run(host="0.0.0.0", port=8080)
