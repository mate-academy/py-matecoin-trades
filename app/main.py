import json
import decimal as d


def calculate_profit(trades_file: None) -> None:
    total_bought = d.Decimal(0)
    total_sold = d.Decimal(0)
    total_amount = d.Decimal(0)
    with open(trades_file, "r") as f:
        trades = json.load(f)

    for trade in trades:
        bought = d.Decimal(trade.get("bought") or 0)
        sold = d.Decimal(trade.get("sold") or 0)
        matecoin_price = d.Decimal(trade.get("matecoin_price") or 0)

        total_bought += bought * matecoin_price
        total_sold += sold * matecoin_price
        total_amount += bought - sold

    profit = {
        "earned_money": str(d.Decimal(total_sold - total_bought)),
        "matecoin_account": str(total_amount)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
