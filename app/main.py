import json
from decimal import Decimal


def calculate_profit(input_file: str) -> None:
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    with open(input_file, "r") as f:
        trades = json.load(f)

    for trade in trades:
        bought = Decimal(trade.get("bought", "0") or "0")
        sold = Decimal(trade.get("sold", "0") or "0")
        matecoin_price = Decimal(trade["matecoin_price"])

        print(
            f"Processing trade: bought={bought}, "
            f"sold={sold}, matecoin_price={matecoin_price}"
        )

        matecoin_account += bought - sold
        earned_money += sold * matecoin_price - bought * matecoin_price

    print(
        f"Calculated profit: earned_money={earned_money}, "
        f"matecoin_account={matecoin_account}"
    )

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
