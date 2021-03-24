import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Pi-Hole blocklist-web'


@app.route('/all.txt')
def blacklist_all():
    return 'pornfile.cz'


if __name__ == '__main__':
    app.run()
