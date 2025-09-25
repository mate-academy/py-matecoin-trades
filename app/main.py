from decimal import Decimal
import json


def calculate_profit(trades_filename: str = "trades.json",
                     profit_filename: str = "profit.json") -> None:
    try:
        with open(trades_filename, "r") as f:
            trades = json.load(f)
    except FileNotFoundError:
        return
    except json.decoder.JSONDecodeError:
        return

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    total_bought = 0
    total_sold = 0
    data_sold = 0
    data_bought = 0
    for trade in trades:
        if trade.get("bought") is not None:
            total_bought += Decimal(trade.get("bought"))
            data_bought += (Decimal(trade.get("matecoin_price"))
                            * Decimal(trade.get("bought")))
        if trade.get("sold") is not None:
            total_sold += Decimal(trade.get("sold"))
            data_sold += (Decimal(trade.get("matecoin_price"))
                          * Decimal(trade.get("sold")))

    matecoin_account = total_bought - total_sold
    earned_money = data_sold - data_bought
    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as outfile:
        json.dump(profit, outfile, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json", "profit.json")
