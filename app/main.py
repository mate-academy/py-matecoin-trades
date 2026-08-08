import json
from decimal import Decimal


def calculate_profit(in_file: str) -> None:
    amount_currency_out = 0
    amount_bought = 0
    amount_currency_in = 0
    amount_sold = 0
    with open(in_file, "r") as file_trades:
        trades = json.load(file_trades)
        for trade in trades:
            matecoin_price = Decimal(trade.get("matecoin_price"))

            if trade.get("bought") is not None:
                amount_bought += Decimal(trade.get("bought"))
                amount_currency_out += (Decimal(trade.get("bought"))
                                        * matecoin_price)

            if trade.get("sold") is not None:
                amount_sold += Decimal(trade.get("sold"))
                amount_currency_in += (Decimal(trade.get("sold"))
                                       * matecoin_price)

    profit_dict = {
        "earned_money": str(amount_currency_in - amount_currency_out),
        "matecoin_account": str(amount_bought - amount_sold)
    }

    with open("profit.json", "w") as file_dump:
        json.dump(profit_dict, file_dump, indent=2)
