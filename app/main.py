import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f, open("profit.json", "a") as p:
        obj = json.load(f)

        coin = decimal.Decimal("0.0")
        money = decimal.Decimal("0.0")

        for i in obj:
            price = decimal.Decimal(i["matecoin_price"])
            if i["bought"]:
                money -= price * decimal.Decimal(i["bought"])
                coin += decimal.Decimal(i["bought"])
            if i["sold"]:
                money += price * decimal.Decimal(i["sold"])
                coin -= decimal.Decimal(i["sold"])

        result = {
            "earned_money": str(money),
            "matecoin_account": str(coin),
        }
        json.dump(result, p, indent=2)


calculate_profit("app/trades.json")
