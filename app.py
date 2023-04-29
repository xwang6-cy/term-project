from flask import Flask, request, jsonify, render_template

from helpers2 import data_display, portfolio_diversification, portfolio_growth, portfolio_risk

app = Flask(__name__)

portfolio = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ticker = request.form["ticker"]
        data = data_display(ticker)
        if "quantity-input" in request.form:
            quantity = request.form["quantity-input"]
            if ticker not in portfolio:
                portfolio[ticker] = int(quantity)
            else:
                portfolio[ticker] += int(quantity)
                
            print(portfolio)
            print(type(portfolio))
        return render_template("stock_info.html", data=data)
    
    return render_template("index.html")
    
@app.route("/my_portfolio")
def my_portfolio():
    portfolio_risk_info = portfolio_risk(portfolio)
    portfolio_growth_info = portfolio_growth(portfolio)
    portfolio_diversification_info = portfolio_diversification(portfolio)

    return render_template('my_portfolio.html', 
                            portfolio=portfolio,
                            portfolio_risk_info=portfolio_risk_info,
                            portfolio_growth_info=portfolio_growth_info,
                            portfolio_diversification_info=portfolio_diversification_info)

if __name__ == '__main__':

    app.run(debug=True)