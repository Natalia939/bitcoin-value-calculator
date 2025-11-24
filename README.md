# Bitcoin Value Calculator

A Python script that calculates the USD value of a specified number of Bitcoins. The script attempts to fetch live Bitcoin prices from the CoinDesk API, but also works offline or if the `requests` library is not installed by asking the user to provide the current rate.

## Features

- Accepts the number of Bitcoins via command-line argument or interactive prompt.
- Fetches live Bitcoin price from CoinDesk API if available.
- Provides interactive fallback if internet is unavailable or `requests` is not installed.
- Calculates and displays the total USD value.
- Robust error handling for invalid input and network/API issues.

## Requirements

- Python 3.x
- Optional: `requests` library (`pip install requests`) for live API fetching

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/bitcoin-value-calculator.git
