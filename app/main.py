import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    earned_money = Decimal("0")
    account_mc = Decimal("0")
    with open(name_file) as f:
        date_trades = json.load(f)
    for i in date_trades:
        if i["bought"] is not None:
            earned_money -= Decimal(i["bought"]) * Decimal(i["matecoin_price"])
            account_mc += Decimal(i["bought"])
        if i["sold"] is not None:
            earned_money += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
            account_mc -= Decimal(i["sold"])
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(account_mc)
    }
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)


calculate_profit("app/trades.json")
