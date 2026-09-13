# OHLCV Downloader from yfinance 


## OHLCV Financial Data Pipeline

A robust, interactive Python script that fetches historical financial market data (Open, High, Low, Close, Volume) using the Yahoo Finance API. It automatically cleans and normalizes the data for professional analysis and allows the user to export the final dataset to a CSV file.

## Features

* **Interactive Asset Menu:** Prompts users to select from a curated list of validated stock and cryptocurrency tickers, preventing invalid inputs.
* **Automated Data Cleaning:** Flattens Yahoo Finance's native MultiIndex output, standardizes all column names to lowercase, and formally sets the DatetimeIndex.
* **Fail-Safe Error Handling:** Safely catches empty downloads or failed API connections and returns the user to the prompt rather than crashing the script.
* **Separation of Concerns:** Data fetching logic is isolated from user input logic, making the core engine entirely reusable for future applications.
* **Dynamic CSV Export:** Gives the user the final choice to keep the data entirely in memory or save it locally with a custom (or dynamically generated) filename.

## Setup & Usage

1. **Install Dependencies:**
   Ensure you have the required libraries installed by running this command in your terminal:
   `pip install yfinance pandas`
2. **Run the Script:**
   Execute the Python file in your terminal.
3. **Follow the Prompts:**
   Select an asset from the provided list, input your exact start and end dates (format: YYYY-MM-DD), and choose whether to export your clean data to a CSV.


NB: The db folder was just created to test out how data looks when pulled from yfinance. That is unprocessed data and of no use for any financial analysis. 
