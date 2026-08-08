import json
import decimal


def calculate_profit(trade_info: str) -> None:
    with open(trade_info, "r") as source_file:
        data = json.load(source_file)

    bank_money = decimal.Decimal("0.0")
    wallet_currency = decimal.Decimal("0.0")
    for item in data:
        if item["sold"]:
            bank_money += (
                decimal.Decimal(item["sold"])
                * decimal.Decimal(item["matecoin_price"])
            )
            wallet_currency -= decimal.Decimal(item["sold"])
        if item["bought"]:
            bank_money -= (
                decimal.Decimal(item["bought"])
                * decimal.Decimal(item["matecoin_price"])
            )
            wallet_currency += decimal.Decimal(item["bought"])

    profit = {
        "earned_money": str(bank_money),
        "matecoin_account": str(wallet_currency),
    }

    with open("profit.json", "w") as final_file:
        json.dump(profit, final_file, indent=2)
