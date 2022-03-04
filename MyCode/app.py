from flask import Flask, redirect, render_template, request, url_for
import yfinance as yf

app = Flask(__name__)
@app.route("/", methods = ["POST", "GET"])
def home():
        if request.method == "POST":
                stockPrediction = request.form["symbol"]
                return redirect(url_for("stockPrediction", sock=stockPrediction))
        else:
                return render_template("index.html")

@app.route("/<sock>")
def stockPrediction(sock):
        try:
                ticker = yf.Ticker(sock)
                pe, eps = ticker.info['trailingPE'], ticker.info['trailingEps']
                price = eps * pe

                price = "The estimated price is " + str(round(price, 2))

                return render_template("stonk.html", price = price)
        except KeyError:
                return render_template("error.html")

        

if __name__ == '__main__':
    app.run()