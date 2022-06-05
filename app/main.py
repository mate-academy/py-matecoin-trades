import json
import decimal as d


def calculate_profit(name_of_file: str):
    with open(name_of_file, "r") as data:

        matecoin_account = 0
        earned_money = 0
        transactions = json.load(data)

        for transaction in transactions:

            price = d.Decimal(transaction["matecoin_price"])

            if transaction["bought"]:

                bought = d.Decimal(transaction["bought"])

                matecoin_account += bought
                earned_money -= bought * price
            else:

                sold = d.Decimal(transaction["sold"])

                matecoin_account -= sold
                earned_money += sold * price

        profit = {"earned_money": f"{earned_money}",
                  "matecoin_account": f"{matecoin_account}"}

        with open("profit.json", "w") as profit_data:
            json.dump([profit], profit_data, indent=2)
