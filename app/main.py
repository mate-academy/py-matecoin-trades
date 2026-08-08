import json

from decimal import Decimal


def profit_in_day(amount: str, matecoin_price: str) -> Decimal:
    return Decimal(amount) * Decimal(matecoin_price)


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin = Decimal("0")
    with open(file_name, "r") as trades_file:
        trades = json.load(trades_file)
        for trade in trades:
            if trade["bought"] is not None:
                earned_money -= profit_in_day(trade["bought"],
                                              trade["matecoin_price"])
                matecoin += Decimal(trade["bought"])
            if trade["sold"] is not None:
                earned_money += profit_in_day(trade["sold"],
                                              trade["matecoin_price"])
                matecoin -= Decimal(trade["sold"])
    with open("profit.json", "w") as profit_file:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin)
        }, profit_file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
