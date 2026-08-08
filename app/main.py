import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        trades = json.load(file)

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

    result_json["matecoin_account"] = str(result_json["matecoin_account"])
    result_json["earned_money"] = str(result_json["earned_money"])

    with open("profit.json", "w") as file:
        json.dump(result_json, file, indent=2)
    print(json.dumps(result_json, indent=2))


if __name__ == "__main__":
    calculate_profit("trades.json")
