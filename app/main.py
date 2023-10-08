import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        buy = 0
        sell = 0
        matecoin_account = 0

        user_data = json.load(file)
        for i in user_data:
            price = decimal.Decimal(i["matecoin_price"])
            if i["bought"] is not None:
                bought = decimal.Decimal(i["bought"])
                buy += bought * price
                matecoin_account += bought

            if i["sold"] is not None:
                sold = decimal.Decimal(i["sold"])
                sell += sold * price
                matecoin_account -= sold

    earned_money = sell - buy
    catalog = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(catalog, file, indent=2)
