import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_read:
        trades_data = json.load(file_read)

        earned_money = decimal.Decimal(0)
        matecoin_account = decimal.Decimal(0)

        for trade in trades_data:
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            if trade["bought"]:
                count_matecoin = decimal.Decimal(trade["bought"])
                money = count_matecoin * matecoin_price
                earned_money -= money
                matecoin_account += count_matecoin
            if trade["sold"]:
                count_matecoin = decimal.Decimal(trade["sold"])
                money = count_matecoin * matecoin_price
                earned_money += money
                matecoin_account -= count_matecoin

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as file_write:
            json.dump(result, file_write, indent=2)
