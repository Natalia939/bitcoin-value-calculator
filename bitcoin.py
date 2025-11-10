import sys

# Try importing requests; if not installed, handle gracefully
try:
    import requests
except ImportError:
    requests = None


def main():
    # Get the number of Bitcoins from command-line argument
    bitcoins = get_bitcoin_amount()

    # Try to fetch live rate from CoinDesk API
    rate = get_bitcoin_rate()

    # Calculate and display total value
    total_cost = bitcoins * rate
    print(f"${total_cost:,.4f}")


def get_bitcoin_amount():
    """Get number of Bitcoins from command-line or prompt user."""
    if len(sys.argv) == 2:
        try:
            return float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number.")
    else:
        # Interactive fallback if no argument provided
        while True:
            try:
                return float(input("Enter number of Bitcoins: "))
            except ValueError:
                print("Invalid input. Enter a number.")


def get_bitcoin_rate():
    """Fetch Bitcoin rate from CoinDesk or ask user if unavailable."""
    if requests:
        try:
            response = requests.get(
                "https://api.coindesk.com/v1/bpi/currentprice.json", timeout=5
            )
            response.raise_for_status()
            data = response.json()
            return data["bpi"]["USD"]["rate_float"]
        except (requests.RequestException, KeyError):
            print("Warning: Unable to fetch Bitcoin price from API.")
    else:
        print("Warning: 'requests' library not installed.")

    # Fallback: prompt user for current rate
    while True:
        try:
            rate = float(input("Enter current Bitcoin rate in USD: "))
            if rate > 0:
                return rate
        except ValueError:
            pass
        print("Invalid rate. Enter a positive number.")


if __name__ == "__main__":
    main()
