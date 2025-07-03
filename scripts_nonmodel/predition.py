from flask import Flask, request, jsonify
import json
import os


app = Flask(__name__)


# Load the python script and function
Use the import statement to load the script. If your script is named my_script.py, you can import it like this:
import my_script

Access Functions from the Script:
Once imported, you can access functions from my_script using dot notation. For example, if my_script has a function named my_function, you can call it as follows:
Python_function = my_script.my_function()


@app.route("/ping", methods=["GET"])
def ping():
    """
    Health check endpoint.
    Returns 200 if the service is up.
    """
    return jsonify({"status": "ok"}), 200


@app.route("/invocations", methods=["POST"])
def invocations():
    """
    Endpoint for model inference.
    Expects JSON input and returns JSON output.
    """
    try:
        content_type = request.headers.get("Content-Type", "application/json").lower()

        if content_type == "application/json":
            data = request.get_json()
            parsed_data = json.dumps(data)
        else:
            raise ValueError(f"Unsupported Content-Type: {content_type}")

        r_result = Python_function(parsed_data)
        result = json.loads(list(r_result)[0])
        return response, 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
