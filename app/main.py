import json
from decimal import Decimal


def calculate_profit(json_trades: str) -> None:
    amount = 0
    amount_of_bought = 0  # how much coin was bought
    amount_after_selling = 0  # how much total coins was sold
    with open(json_trades, "r") as file:
        json_data = json.load(file)
        for trade in json_data:
            matecoin_price = Decimal(trade.get("matecoin_price"))
            if not trade.get("bought") is None:
                bought = Decimal(trade.get("bought"))
                amount += bought
                amount_of_bought += bought * matecoin_price
            if not trade.get("sold") is None:
                sold = Decimal(trade.get("sold"))
                amount_after_selling += matecoin_price * sold
                amount -= sold
    profit_dict = {
        "earned_money": str(amount_after_selling - amount_of_bought),
        "matecoin_account": str(amount)
    }

    with open("profit.json", "w") as dump_file:
        json.dump(profit_dict, dump_file, indent=2)
