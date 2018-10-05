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
    try:
        yahoo = Share(symbol)
        name = yahoo.get_name()
        price = yahoo.get_price()
    except:
        return None
    return {
        "name": name,
        "price": price,
        "symbol": symbol.upper()
    }


@app.route("/")
@login_required
def index():
    portfolio_symbols = cursor.execute("SELECT shares, symbols FROM portfolio WHERE id = :id", id = session["user_id"])
    total_cash = 0
    for portfolio_symbol in portfolio_symbols:
        symbol = portfolio_symbol["symbol"]
        shares = portfolio_symbol["shares"]
        stock = lookup(symbol)
        total = shares * stock["price"]
        total_cash += total
        cursor.execute("UPDATE portfolio SET price = :price, total = :total WHERE id=:id AND symbol=:symbol", price=usd(stock["price"]), total=usd(total), id=session["user_id"], symbol=symbol)
    
    updated_cash = cursor.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
    total_cash += updated_cash[0]["cash"]
    updated_portfolio = cursor.execute("SELECT * from portfolio WHERE id=:id", id=session["user_id"])
    return render_template("index.html", stocks=updated_portfolio, cash=usd(updated_cash[0]["cash"]), total= usd(total_cash))
    # return "Welcome!"


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""

    if request.method == "GET":
        return render_template("buy.html")
    else:
        # ensure proper symbol
        stock = lookup(request.form.get("symbol"))
        if not stock:
            return apology("Invalid Symbol")

        # ensure proper number of shares
        try:
            shares = int(request.form.get("shares"))
            if shares < 0:
                return apology("Shares must be positive integer")
        except:
            return apology("Shares must be positive integer")

        # select user's cash
        money = cursor.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])

        # check if enough money to buy
        if not money or float(money[0]["cash"]) < stock["price"] * shares:
            return apology("Not enough money")

        # update history
        cursor.execute("INSERT INTO histories (symbol, shares, price, id, transacted) VALUES(:symbol, :shares, :price, :id, DateTime('now'))", symbol=stock["symbol"], shares=shares, price=usd(stock["price"]), id=session["user_id"])

        # update user cash
        cursor.execute("UPDATE users SET cash = cash - :purchase WHERE id = :id", id=session["user_id"], purchase=stock["price"] * float(shares))

        # Select user shares of that symbol
        user_shares = cursor.execute("SELECT shares FROM portfolio WHERE id = :id AND symbol=:symbol", id=session["user_id"], symbol=stock["symbol"])

        # if user doesn't has shares of that symbol, create new stock object
        if not user_shares:
            cursor.execute("INSERT INTO portfolio (name, shares, price, total, symbol, id) VALUES(:name, :shares, :price, :total, :symbol, :id)", name=stock["name"], shares=shares, price=usd(stock["price"]), total=usd(shares * stock["price"]), symbol=stock["symbol"], id=session["user_id"])

        # Else increment the shares count
        else:
            shares_total = user_shares[0]["shares"] + shares
            cursor.execute("UPDATE portfolio SET shares=:shares WHERE id=:id AND symbol=:symbol", shares=shares_total, id=session["user_id"], symbol=stock["symbol"])

        # return to index
        return redirect(url_for("index"))


@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    histories = cursor.execute("SELECT * from histories WHERE id=:id", id=session["user_id"])

    return render_template("history.html", histories=histories)