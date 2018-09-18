from flask import Flask
from flaskext.mysql import MySQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run()