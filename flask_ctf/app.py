from flask import Flask, jsonify

with open("a/secrets.txt") as f:
    secret = f.read()
    secret = "fl4g{" + secret + "}"

with open("b/secrets.txt") as f:
    route = f.read()
    print(route)

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Not here!</h1>"


@app.route("/secrets/<name>")
def hello(name):
    if name.strip() == route.strip():
        return f"The secret is:<h1>{secret}</h1>"
    else:
        return "<h1>Not here!</h1>"


if __name__ == "__main__":
    app.run()
