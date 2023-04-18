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
        return render_template("stock_info.html", data=data)
    return render_template("index.html")
    

@app.route("/my_portfolio")
def my_portfolio():
    # Calculate portfolio growth
    growth_rate = portfolio_growth(portfolio)
    if growth_rate is None:
        # Handle the ZeroDivisionError by returning a default value, raising an exception, or providing a user-friendly message
        return "Unable to calculate portfolio growth rate. The portfolio has no value or it had no value in the previous period."

    # Evaluate portfolio diversification
    diversification_dict = portfolio_diversification(portfolio)
    if diversification_dict is None:
        # Handle the ZeroDivisionError by returning a default value, raising an exception, or providing a user-friendly message
        return "Unable to calculate portfolio diversiation_dict. The portfolio has no value or it had no value in the previous period."

    # Evaluate portfolio risk
    portfolio_risk_stats = portfolio_risk([{'ticker': t, 'quantity': q} for t, q in portfolio.items()])
    if diversification_dict is None:
        # Handle the ZeroDivisionError by returning a default value, raising an exception, or providing a user-friendly message
        return "Unable to calculate portfolio portofilo risk stats. The portfolio has no value or it had no value in the previous period."

    # Render the portfolio template with the necessary data
    return render_template('my_portfolio.html', 
                           portfolio=portfolio, 
                           growth_rate=growth_rate,
                           diversification=diversification_dict, 
                           portfolio_risk_stats=portfolio_risk_stats)

if __name__ == '__main__':
    app.run(debug=True)