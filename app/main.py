import json
import decimal


def calculate_profit(file_json: str) -> None:
    with open(file_json, "r") as file:
        trades = json.load(file)
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades:
        dec_matecoin_price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"]:
            dec_bought = decimal.Decimal(trade["bought"])
            earned_money -= dec_bought * dec_matecoin_price
            matecoin_account += dec_bought
        if trade["sold"]:
            dec_sold = decimal.Decimal(trade["sold"])
            earned_money += dec_sold * dec_matecoin_price
            matecoin_account -= dec_sold

    final_report = {"earned_money": str(earned_money),
                    "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as f:
        json.dump(final_report, f, indent=2)
