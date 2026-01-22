import json
import decimal


def calculate_profit(input_file_name: str) -> None:
    count_money = decimal.Decimal("0")
    count_coins = decimal.Decimal("0")

    with open(input_file_name, "r") as file:
        list_trades = json.load(file)
        for dic in list_trades:
            if dic["bought"] is not None:
                count_coins += decimal.Decimal(dic["bought"])
                count_money -= decimal.Decimal(dic["bought"]) \
                    * decimal.Decimal(dic["matecoin_price"])

            if dic["sold"] is not None:
                count_coins -= decimal.Decimal(dic["sold"])
                count_money += decimal.Decimal(dic["sold"]) \
                    * decimal.Decimal(dic["matecoin_price"])

    result = {
        "earned_money": str(count_money),
        "matecoin_account": str(count_coins)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    calculate_profit()
