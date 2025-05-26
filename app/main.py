import json
from decimal import Decimal


def calculate_profit(file_name: str = "trades.json") -> None:

    data = json.load(open(file_name))
    data_bought = []
    data_sold = []
    account_bought = []
    account_sold = []

    for i in data:
        price = Decimal(i["matecoin_price"])
        if i["bought"]:
            bought = Decimal(i["bought"])
            data_bought.append(bought * price)
            account_bought.append(bought)
        if i["sold"]:
            sold = Decimal(i["sold"])
            data_sold.append(sold * price)
            account_sold.append(sold)

    matecoin_account = (sum(account_bought) - sum(account_sold))
    earned_money = (sum(data_bought) - sum(data_sold))

    new_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file:
        json.dump(new_data, file, indent=2)
