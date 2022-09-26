import json
import decimal as d


def calculate_profit(file: str) -> None:
    with open(file) as f:
        trades = json.load(f)
    matecoin_acccount = 0
    earned_money = 0
    for operation in trades:
        price = d.Decimal(operation["matecoin_price"])
        if operation["bought"]:
            earned_money -= d.Decimal(operation["bought"]) * price
            matecoin_acccount += d.Decimal(operation["bought"])
        if operation["sold"]:
            earned_money += d.Decimal(operation["sold"]) * price
            matecoin_acccount -= d.Decimal(operation["sold"])
    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_acccount)}
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
