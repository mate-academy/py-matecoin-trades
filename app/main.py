import json
import decimal


def calculate_profit(trades_info: str) -> None:
    with open(trades_info, "r") as file:
        trades_list = json.load(file)
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for trade in trades_list:
        if trade["sold"] is not None:
            sold = (
                decimal.Decimal(trade["sold"])
                * decimal.Decimal(trade["matecoin_price"])
            )
            earned_money += sold
            matecoin_account -= decimal.Decimal(trade["sold"])
        if trade["bought"] is not None:
            sold = (
                decimal.Decimal(trade["bought"])
                * decimal.Decimal(trade["matecoin_price"])
            )
            earned_money -= sold
            matecoin_account += decimal.Decimal(trade["bought"])
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
