import decimal
import json


def calculate_profit(file_name: str = "trades.json") -> None:
    with open(file_name, "r") as f:
        data_history = json.load(f)
    matecoin_account = decimal.Decimal("0")
    earned_money = decimal.Decimal("0")

    for trade in data_history:
        price = decimal.Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            buy_amount = decimal.Decimal(trade["bought"])
            matecoin_account += buy_amount
            earned_money -= buy_amount * price

        if trade["sold"] is not None:
            sell_amount = decimal.Decimal(trade["sold"])
            matecoin_account -= sell_amount
            earned_money += sell_amount * price

    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account), }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
