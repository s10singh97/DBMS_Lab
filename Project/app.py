from flask import Flask
from flaskext.mysql import MySQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from yahoo_finance import Share
from tempfile import gettempdir
from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'shiman97'
app.config['MYSQL_DATABASE_DB'] = 'shrtrade'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

def lookup(symbol):
    yahoo = Share(symbol)
    quote = yahoo.get_price()
    return quote


@app.route("/")
# @login_required
def index():
    portfolio_symbols = cursor.execute("SELECT shares, symbols FROM portfolio WHERE id = :id", id = session["user_id"])
    total_cash = 0
    for portfolio_symbol in portfolio_symbols:
        symbol = portfolio_symbol["symbol"]
        shares = portfolio_symbol["shares"]
        stock = lookup(symbol)
        total = shares * stock["price"]
        total_cash += total
        cursor.execute("UPDATE portfolio SET price = :price, total = :total WHERE id=:id AND symbol=:symbol", price=usd(stock), total=usd(total), id=session["user_id"], symbol=symbol)
    
    updated_cash = cursor.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
    total_cash += updated_cash[0]["cash"]
    updated_portfolio = cursor.execute("SELECT * from portfolio WHERE id=:id", id=session["user_id"])
    return render_template("index.html", stocks=updated_portfolio, cash=usd(updated_cash[0]["cash"]), total= usd(total_cash))
    # return "Welcome!"

