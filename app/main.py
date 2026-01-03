import json

from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(f"{trades_file}", "r") as file:
        trades = json.load(file)

    cash = Decimal("0")
    account = Decimal("0")

    for transaction in trades:
        price = Decimal(transaction["matecoin_price"])

        if transaction["bought"] is not None:
            buy = Decimal(transaction["bought"])
            account += buy
            spent = buy * price
            cash -= spent

        if transaction["sold"] is not None:
            sell = Decimal(transaction["sold"])
            account -= sell
            earned = sell * price
            cash += earned

    result = {
        "earned_money": str(cash),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as profit:
        json.dump(result, profit, indent=2)
