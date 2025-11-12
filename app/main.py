import json
from decimal import Decimal


def get_a_trades() -> list:
    with open("trades.json", "r") as file:
        trades = json.load(file)
    return trades

def write_trades(trades: dict) -> None:
    with open("profit.json", "w") as file:
        json.dump(trades, file, indent=2, default=str)
    print(json.dumps(trades, indent=2, default=str))

def calculate_profit() -> None:
    trades = get_a_trades()
    result_json = {"earned_money": 0, "matecoin_account": 0}

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        # Якщо купуємо (bought != None)
        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            result_json["matecoin_account"] += amount
            result_json["earned_money"] -= price * amount

        # Якщо продаємо (sold != None)
        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            result_json["matecoin_account"] -= amount
            result_json["earned_money"] += price * amount

    write_trades(result_json)

if __name__ == "__main__":
    calculate_profit()