import json
import decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file) as data:
        open_file = json.load(data)
    earned_money = 0
    matecoin_account = 0
    for i in open_file:
        if i["bought"] is None:
            i["bought"] = 0
        if i["sold"] is None:
            i["sold"] = 0
    for dic in open_file:
        coin = decimal.Decimal(dic["bought"]) - decimal.Decimal(dic["sold"])
        earned_money -= decimal.Decimal(coin)\
            * decimal.Decimal(dic["matecoin_price"])
        matecoin_account += decimal.Decimal(coin)

    fil = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit:
        json.dump(fil, profit, indent=2)


if __name__ == "__main__":
    print(calculate_profit("trades.json"))
