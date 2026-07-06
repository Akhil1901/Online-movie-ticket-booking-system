from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is Working!"

if __name__ == "__main__":
    print("Starting Test Server...")
    app.run(host="127.0.0.1", port=8000, debug=False)