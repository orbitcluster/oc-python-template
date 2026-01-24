from flask import Flask, jsonify
import os
import yaml

app = Flask(__name__)


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


config = load_config()


@app.route("/")
def home():
    return jsonify({"message": "Hello from the Flask Boilerplate Project!!"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/config")
def get_config():
    # WARNING: This exposes secrets! Only for demonstration purposes.
    return jsonify(config)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
