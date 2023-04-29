import yfinance as yf
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io
import base64


def get_stock_info(ticker) -> dict:
    """
    Fetch historical stock data from Yahoo Finance based on the ticker input.

    Parameters:
        ticker (str): The stock ticker symbol

    Returns:
        dict: A dictionary containing relevant stock information
    """
    # Use built-in Yahoo finance libarayr to retrieve the stock information
    stock = yf.Ticker(ticker)

    # Store the stock information in variable info
    info = stock.info

    # Get historical market data for the past month
    hist = stock.history(period="1mo")

    # Get income statement and balance sheet data
    # income_stmt = stock.financials
    # balance_sheet = stock.balance_sheet

    # from stock info, extract the following information
    currency = info["currency"]
    exchange = info["exchange"]
    name = info["shortName"]

    # Format historical market data as a string
    hist_str = "\nHistorical Market Data (Past Month):\n" + hist.to_string()

    # Create dictionary with relevant stock information
    stock_info = {
        "name": name,
        "ticker": ticker,
        "currency": currency,
        "exchange": exchange,
        "hist": hist,
        "info": info,
    }

    # return the dictionary
    return stock_info


# print(get_stock_info("AAPL"))
def data_display(ticker) -> dict:
    """
    Parse and display stock data and extract relevant information: the company description, growth graph to display to the user

    Parameters:
        ticker (str): The stock ticker symbol

    Returns:
        dict: A dictionary containing company description and historical market data
    """
    # Get relevant stock information
    stock_info = get_stock_info(ticker)

    # Extrat the information from stock_info
    name = stock_info["name"]
    ticker = stock_info["ticker"]
    currency = stock_info["currency"]
    exchange = stock_info["exchange"]
    hist = stock_info["hist"]
    info = stock_info["info"]
    # Print out company description
    # print(f"{name} ({ticker}) is traded on {exchange} in {currency}. {info['longBusinessSummary']}\n")

    # Plot historical market data
    plt.plot(hist["Close"])
    plt.title(f"{name} ({ticker}) Historical Close Price")
    plt.xlabel("Date")
    plt.ylabel(f"Close Price ({currency})")

    # Convert plot to PNG image
    img_data = io.BytesIO()
    plt.savefig(img_data, format="png")
    img_data.seek(0)
    encoded_img = base64.b64encode(img_data.getvalue()).decode()

    # Create dictionary with company description and historical market data
    data_dict = {
        "company": {
            "name": name,
            "ticker": ticker,
            "currency": currency,
            "exchange": exchange,
            "description": info["longBusinessSummary"],
        },
        "historical_data": hist,
        "image_data": encoded_img,
    }

    # Return the dictionary
    return data_dict


import pandas as pd
import numpy as np


def portfolio_risk(portfolio):
    """
    This function will evaluate the risk of a portfolio by calculating its variance and covariance.
    Parameters:
        portfolio (dict): A dictionary representing the portfolio, where each key is a ticker symbol and each value is the quantity of the corresponding stock.
    Returns:
        tuple: A tuple containing the portfolio variance and covariance.
    """
    # Create an empty list that stores the market data
    prices = {}

    # Convert the portolio quanities into a numpy arrary
    weights = np.array(list(portfolio.values()))

    # For every stock in the portfolio, obatin the market data using function get stock info and store it the price dictionary
    for ticker, quantity in portfolio.items():
        hist = get_stock_info(ticker)["hist"]
        prices[ticker] = hist["Close"] * quantity

    # Convert the price dictionary into pandas dataframe
    prices_df = pd.DataFrame(prices.values()).transpose()

    # Calculate the change of price over time while removing rows with na values
    returns_df = prices_df.pct_change().dropna()

    # Calculate portfolio variance and covariance
    cov_matrix = returns_df.cov()
    var_portfolio = np.dot(weights.T, np.dot(cov_matrix, weights))

    # Calculate the covariance between each pair of stocks in the portfolio
    variances = np.diag(cov_matrix.values)
    covariance = []
    for i in range(len(variances)):
        for j in range(i + 1, len(variances)):
            cov = cov_matrix.iloc[i, j] * variances[i] * variances[j]
            covariance.append(cov)

    # calculate the totak risk of the portfolio by adding the variance and coavariance
    risk = (var_portfolio + np.sum(covariance)) * 100

    # Return the risk as a tuple and round it to 6 decimal places
    return round(risk, 6)


def portfolio_growth(portfolio):
    """
    This function will use historical stock price data of a portfolio to calculate the projected growth rate.

    Parameters:
        portfolio (dict): A dictionary containing stocks in the portfolio and their quantities.
            Example: {'AAPL': 10, 'GOOG': 5, 'MSFT': 20}

    Returns:
        float: The projected growth rate of the portfolio based on historical stock data
    """
    # Delcare the total value and total cost variables
    total_value = 0
    total_cost = 0

    # Iterate through all of the items in portfolio dictionary
    for stock, quantity in portfolio.items():

        # Get historical market data for the stock
        hist = yf.Ticker(stock).history(period="1mo")

        # Get the latest close price of the stock
        latest_price = hist["Close"].iloc[-1]

        # Calculate the total value and cost of the stock in the portfolio
        stock_value = latest_price * quantity
        stock_cost = hist["Close"].iloc[0] * quantity
        total_value += stock_value
        total_cost += stock_cost

    # Calculate the growth rate as the ratio of total value to total cost
    growth_rate = (total_value - total_cost) / total_cost

    # Return the growth rate in terms of percenatge value and round it to 6
    return round(growth_rate * 100, 6)


def portfolio_diversification(portfolio):
    """
    Calculate the industry information of the stocks in the portfolio to show diversification.

    Parameters:
        portfolio (dict): A dictionary containing stocks in the portfolio and their quantities.
            Example: {'AAPL': 10, 'GOOG': 5, 'MSFT': 20}

    Returns:
        str: A string containing the portfolio diversification by industry.
    """
    # Initializes an empty dictonary to store industry information
    industries = {}

    # Iterate through all of the items in portoflio dictionary
    for stock, quantity in portfolio.items():

        # Get industry information for the stock using get stock info function
        stock_info = get_stock_info(stock)
        industry = stock_info["info"].get("industry")

        # Add the quanity of the stock to the corresponding industry category
        if industry:
            if industry in industries:
                industries[industry] += quantity
            else:
                industries[industry] = quantity

    # If there are no industry information for any of the stock, then return the string
    if not industries:
        return "No industry information available for the stocks in the portfolio."

    ## calculate the total quanity of the stocks in the portfolio
    total_quantity = sum(industries.values())

    diversification_info = "Portfolio Diversification by Industry:\n"

    # calculate the percentage of shares in each indursty category
    for industry, quantity in industries.items():
        percentage = (quantity / total_quantity) * 100
        diversification_info += f"- {industry}: {quantity} shares ({percentage:.2f}%)\n"

    # Return the final string containing the diversifcation
    return diversification_info


def main():
    data = data_display("AAPL")
    print(data)
    data_display("AAPL")


if __name__ == "__main__":
    main()
