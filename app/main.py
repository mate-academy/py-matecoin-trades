import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file_in:
        trades = json.load(file_in)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades:
        if trade["bought"]:
            matecoin_account += decimal.Decimal(trade["bought"])
            earned_money -= (
                decimal.Decimal(trade["bought"])
                * decimal.Decimal(trade["matecoin_price"])
            )
        if trade["sold"]:
            matecoin_account -= decimal.Decimal(trade["sold"])
            earned_money += (
                decimal.Decimal(trade["sold"])
                * decimal.Decimal(trade["matecoin_price"])
            )

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file_out:
        json.dump(profit_data, file_out, indent=2)
