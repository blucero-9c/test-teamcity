from flask import Flask
import os
import re

app = Flask(__name__)


def valid_hex(h):
    return bool(re.fullmatch(r'#([0-9a-fA-F]{6})', h))


@app.route('/')
def home():
    color = os.environ.get('BG_COLOR', '#00ff00')

    # simple validation: if invalid, return 500 (this is for testing failing conditions)
    if not valid_hex(color):
        return "Invalid color", 500

    html = f"<html><body style='background-color:{color};height:100vh;'></body></html>"
    return html, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
