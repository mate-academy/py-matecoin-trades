import json
import decimal


def calculate_profit(
        trades_file_path: str,
        profit_file_path: str = "profit.json"
) -> None:

    with open(trades_file_path, "r") as file:
        trades = json.load(file)

    matecoin_account = decimal.Decimal("0")
    earned_money = decimal.Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            dec_bought = decimal.Decimal(trade["bought"])
            dec_matecoin_price = decimal.Decimal(trade["matecoin_price"])
            matecoin_account += dec_bought
            earned_money -= dec_bought * dec_matecoin_price
        if trade["sold"] is not None:
            dec_sold = decimal.Decimal(trade["sold"])
            dec_matecoin_price = decimal.Decimal(trade["matecoin_price"])
            matecoin_account -= dec_sold
            earned_money += dec_sold * dec_matecoin_price

    trades_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(profit_file_path, "w") as profit_file:
        json.dump(trades_dict, profit_file, indent=2)
