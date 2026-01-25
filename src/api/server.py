from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Hello from the Flask Boilerplate Project!!"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


from flask import request
@app.route("/vulnerable")
def vulnerable():
    # INTENTIONAL VULNERABILITY: CWE-78 (OS Command Injection)
    # This should be caught by CodeQL
    user_input = request.args.get("cmd", "")
    os.system("echo " + user_input)
    return jsonify({"status": "executed"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
