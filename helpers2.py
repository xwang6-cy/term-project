import yfinance as yf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io 
import base64

def get_stock_info(ticker):
    """
    Fetch historical stock data from Yahoo Finance based on the ticker input.
    
    Parameters:
        ticker (str): The stock ticker symbol
        
    Returns:
        dict: A dictionary containing relevant stock information
    """
    stock = yf.Ticker(ticker)
    info = stock.info
    
    # Get historical market data for the past month
    hist = stock.history(period="1mo")
    
    # Get income statement and balance sheet data
    # income_stmt = stock.financials
    # balance_sheet = stock.balance_sheet
    
    currency = info['currency']
    exchange = info['exchange']
    name = info['shortName']
    
    # Format historical market data as a string
    hist_str = '\nHistorical Market Data (Past Month):\n' + hist.to_string()
    
    # Create dictionary with relevant stock information
    stock_info = {
        'name': name,
        'ticker': ticker,
        'currency': currency,
        'exchange': exchange,
        'hist': hist,
        'info': info
    }
    
    return stock_info

# print(get_stock_info("AAPL"))
def data_display(ticker):
    """
    Parse and display stock data and extract relevant information: the company description, growth graph to display to the user
    
    Parameters:
        ticker (str): The stock ticker symbol
        
    Returns:
        dict: A dictionary containing company description and historical market data
    """
    # Get relevant stock information
    stock_info = get_stock_info(ticker)
    
    name = stock_info['name']
    ticker = stock_info['ticker']
    currency = stock_info['currency']
    exchange = stock_info['exchange']
    hist = stock_info['hist']
    info = stock_info['info']
    # Print out company description
    # print(f"{name} ({ticker}) is traded on {exchange} in {currency}. {info['longBusinessSummary']}\n")
    
    # Plot historical market data
    plt.plot(hist['Close'])
    plt.title(f"{name} ({ticker}) Historical Close Price")
    plt.xlabel("Date")
    plt.ylabel(f"Close Price ({currency})")

    # Convert plot to PNG image
    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    encoded_img = base64.b64encode(img_data.getvalue()).decode()
    
    
    # Create dictionary with company description and historical market data
    data_dict = {
        'company': {
            'name': name,
            'ticker': ticker,
            'currency': currency,
            'exchange': exchange,
            'description': info['longBusinessSummary']
        },
        'historical_data': hist,
        'image_data': encoded_img
    }
    
    return data_dict


def portfolio_growth(portfolio):
    """
    This function will use historical stock price data of a portfolio to calculate the projected growth rate.
    
    Parameters:
        portfolio (dict): A dictionary containing stocks in the portfolio and their quantities.
            Example: {'AAPL': 10, 'GOOG': 5, 'MSFT': 20}
    
    Returns:
        float: The projected growth rate of the portfolio based on historical stock data
    """
    total_value = 0
    total_cost = 0
    for stock, quantity in portfolio.items():
        # Get historical market data for the stock
        hist = yf.Ticker(stock).history(period="1mo")
        # Get the latest close price of the stock
        latest_price = hist['Close'].iloc[-1]
        # Calculate the total value and cost of the stock in the portfolio
        stock_value = latest_price * quantity
        stock_cost = hist['Close'].iloc[0] * quantity
        total_value += stock_value
        total_cost += stock_cost
    # Calculate the growth rate as the ratio of total value to total cost
    growth_rate = (total_value - total_cost) / total_cost
    return growth_rate

# print(portfolio_growth({'AAPL': 10, 'GOOG': 5, 'MSFT': 20}))

def portfolio_diversification(portfolio):
    """
    This function will evaluate the diversification of a portfolio across different sectors, industries, and asset classes.
    
    Parameters:
        portfolio (dict): A dictionary containing stocks in the portfolio and their quantities.
            Example: {'AAPL': 10, 'GOOG': 5, 'MSFT': 20}
    
    Returns:
        dict: A dictionary containing the diversification of the portfolio across sectors, industries, and asset classes
    """
    # Get information for each stock in the portfolio
    stock_infos = []
    for stock in portfolio.keys():
        # name = stock_info['name']
        # ticker = stock_info['ticker']
        # currency = stock_info['currency']
        # exchange = stock_info['exchange']
        # hist = stock_info['hist']
        # info = stock_info['info']
        stock_info = get_stock_info(stock)
        stock_infos.append(stock_info)
    # Extract sector, industry, and asset class information for each stock
    sectors = set([info['info']['sector'] for info in stock_infos])
    industries = set([info['info']['industry'] for info in stock_infos])
    asset_classes = set([info['info']['quoteType'] for info in stock_infos])
    # Calculate the proportion of the portfolio in each sector, industry, and asset class
    total_value = sum([info['hist']['Close'].iloc[-1] * quantity for stock, quantity in portfolio.items()])
    sector_values = {}
    industry_values = {}
    asset_class_values = {}
    for info, quantity in zip(stock_infos, portfolio.values()):
        value = info['hist']['Close'].iloc[-1] * quantity
        sector = info['info']['sector']
        industry = info['info']['industry']
        asset_class = info['info']['quoteType']
        if sector in sector_values:
            sector_values[sector] += value
        else:
            sector_values[sector] = value
        if industry in industry_values:
            industry_values[industry] += value
        else:
            industry_values[industry] = value
        if asset_class in asset_class_values:
            asset_class_values[asset_class] += value
        else:
            asset_class_values[asset_class] = value
    sector_proportions = {sector: value / total_value for sector, value in sector_values.items()}
    industry_proportions = {industry: value / total_value for industry, value in industry_values.items()}
    asset_class_proportions = {asset_class: value / total_value for asset_class, value in asset_class_values.items()}
    # Create dictionary with diversification information
    diversification_dict = {
        'sectors': sector_proportions,
        'industries': industry_proportions,
        'asset_classes': asset_class_proportions
    }
    return diversification_dict
       
# print(portfolio_diversification({'AAPL': 10, 'GOOG': 5, 'MSFT': 20}))

def portfolio_risk(portfolio):
    """
    This function will evaluate the risk of portfolio by caculating its variance and covariance
    
    Parameters:
        portfolio (list): A list of dictionaries representing the portfolio, where each dictionary contains 'ticker' and 'quantity' keys
        
    Returns:
        tuple: A tuple containing the portfolio variance and covariance
    """
    prices = {}
    for stock in portfolio:
        ticker = stock['ticker']
        quantity = stock['quantity']
        hist = get_stock_info(ticker)['hist']
        prices[ticker] = hist['Close'] * quantity
    
    prices_df = pd.DataFrame(prices)
    returns_df = prices_df.pct_change().dropna()

    total_value = sum([get_stock_info(stock['ticker'])['hist']['Close'] * stock['quantity'] for stock in portfolio]) 
    weights = np.array([stock['quantity'] / total_value for stock in portfolio]) 
    
    # Calculate portfolio variance and covariance
    cov_matrix = returns_df.cov()
    var_portfolio = np.dot(weights.T, np.dot(cov_matrix, weights))
    variances = np.diag(cov_matrix.values)
    covariance = []
    for i in range(len(variances)):
        for j in range(i+1, len(variances)):
            cov = cov_matrix.iloc[i,j] * variances[i] * variances[j] ** 0.5
            covariance.append(cov)

    return (var_portfolio, sum(covariance))

import sqlite3

def data_store(portfolio_name, portfolio_return, portfolio_risk, portfolio_diversity):
    """
    Store portfolio information in an SQLite database
    
    Parameters:
        portfolio_name (str): The name of the portfolio
        portfolio_return (float): The return of the portfolio
        portfolio_risk (float): The risk of the portfolio
        portfolio_diversity (dict): A dictionary containing the diversification of the portfolio
        
    Returns:
        None
    """
    # Connect to database
    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()
    
    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS portfolios
                 (name text, return real, risk real, diversity text)''')
    
    # Insert portfolio information into table
    c.execute("INSERT INTO portfolios VALUES (?, ?, ?, ?)", (portfolio_name, portfolio_return, portfolio_risk, str(portfolio_diversity)))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

def main():
    data = data_display('AAPL')
    print(data)
    data_display("AAPL")


if __name__ == "__main__":
    main()
