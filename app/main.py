import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    try:
        with open(trades_file, "r") as file:
            trades = json.load(file)
    except FileNotFoundError:
        print(f"Помилка: Файлу {trades_file} не існує.")
        return

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:

        price = Decimal(trade["matecoin_price"])

        if trade.get("bought") is not None:
            volume = Decimal(trade["bought"])
            earned_money -= volume * price
            matecoin_account += volume

        if trade.get("sold") is not None:
            volume = Decimal(trade["sold"])
            earned_money += volume * price
            matecoin_account -= volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
