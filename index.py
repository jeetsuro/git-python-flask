from flask import Flask

# https://www.wintellect.com/containerize-python-app-5-minutes/

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!!!!!!!.."
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)