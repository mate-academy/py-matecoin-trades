import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    """
        Calculate profit from Matecoin trades and save results to profit.json.
    :param filename: Path to json file containin trade history.
    """

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    try:
        with open(filename, "r") as f:
            trades = json.load(f)

        for trade in trades:
            bougt = Decimal(trade["bought"]) \
                if trade["bought"] else Decimal("0")
            sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
            price = Decimal(trade["matecoin_price"])

            matecoin_account += bougt - sold
            earned_money -= (bougt - sold) * price

            result = {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            }

        with open("profit.json", "w") as f:
            json.dump(result, f, indent=2)

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid json format in '{filename}'")
    except KeyError as e:
        print(f"Error: Missing required field in trade data - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


calculate_profit("trades.json")
