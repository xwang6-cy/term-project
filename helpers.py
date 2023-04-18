from flask import Flask, request, jsonify, render_template
import requests

RAPIDAPI_KEY = "c72f7a4367mshfe65ee4a74a894fp176ec0jsn93a89c3102d3"


def get_ticker_symbol(company_name):

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"
    params = {
        "q": company_name.lower(),
        "region": "US"
    }
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY
    }
    response = requests.get(url, params=params, headers=headers)
    response_json = response.json()
    
    if "quotes" in response_json:
        return response_json["quotes"][0]["symbol"]
    else:
        return None

def get_stock_info(ticker_symbol):

    url = f"https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary?symbol={ticker_symbol}&region=US"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY
    }
    response = requests.get(url, headers=headers)
    response_json = response.json()
    if "price" in response_json and "summaryDetail" in response_json:
        return {
            "name": response_json["price"]["longName"],
            "price": response_json["price"]["regularMarketPrice"]["fmt"],
            "currency": response_json["price"]["currency"],
            "market_cap": response_json["summaryDetail"]["marketCap"]["fmt"],
            "pe_ratio": response_json["summaryDetail"]["trailingPE"]["fmt"]
        }
    
    else:
        return None

def main():
    print(get_stock_info('APPL'))


if __name__ == "__main__":
    main()