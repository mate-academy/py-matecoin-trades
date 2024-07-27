import json
import decimal


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file, "r") as file_in:
        trades = json.load(file_in)

    earned_money = decimal.Decimal("0")
    coins_owned = decimal.Decimal("0")
    for trade in trades:
        if trade["bought"] is not None:
            price = decimal.Decimal(str(trade["bought"])) * decimal.Decimal(str(trade["matecoin_price"]))
            coins_owned += decimal.Decimal(str(trade["bought"]))
            earned_money -= price
        if trade["sold"] is not None:
            price = decimal.Decimal(str(trade["sold"])) * decimal.Decimal(str(trade["matecoin_price"]))
            coins_owned -= decimal.Decimal(str(trade["sold"]))
            earned_money += price

    total = {
        "earned_money": str(earned_money),
        "matecoin_account": str(coins_owned),
    }
    with open("profit.json", "w") as file_out:
        json.dump(total, file_out, indent=2)
