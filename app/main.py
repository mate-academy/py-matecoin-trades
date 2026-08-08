import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

    earned = Decimal(0)
    spent = Decimal(0)
    matecoin_balance = Decimal(0)

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought:
            spent += Decimal(bought) * matecoin_price
            matecoin_balance += Decimal(bought)

        if sold:
            earned += Decimal(sold) * matecoin_price
            matecoin_balance -= Decimal(sold)

    total_earned = earned - spent

    result = {
        "earned_money": str(total_earned),
        "matecoin_account": str(matecoin_balance)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
