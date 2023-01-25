from flask import Flask

app = Flask(__name__)


@app.route('/ping')
def ping():
    return "<h3>I'm pinging in the rain ...</h3>"

app.add_url_rule("/", endpoint="ping")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
