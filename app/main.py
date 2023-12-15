import json
import decimal


def calculate_profit(file_name: str) -> None:
    money = decimal.Decimal("0")
    matecoins_available = decimal.Decimal("0")
    with open(file_name) as file:
        trades = json.load(file)
        for trade in trades:
            if trade["bought"]:
                matecoins_available += decimal.Decimal(trade["bought"])
                money -= (decimal.Decimal(trade["bought"])
                          * decimal.Decimal(trade["matecoin_price"]))
            if trade["sold"]:
                matecoins_available -= decimal.Decimal(trade["sold"])
                money += (decimal.Decimal(trade["sold"])
                          * decimal.Decimal(trade["matecoin_price"]))

    result = {
        "earned_money": str(money),
        "matecoin_account": str(matecoins_available)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
