import json
from decimal import Decimal


def calculate_profit(file_name: str = "trades.json" ):

    data = json.load(open("trades.json"))
    data_bought =[]
    data_sold = []
    account_bought = []
    account_sold = []
    new_data = []

    for i in data:
        if i["bought"] == None:
            continue
        else:
            price_bought = Decimal(float(i["bought"])) * Decimal(float(i["matecoin_price"]))
            data_bought.append(price_bought)
            account_bought.append(float(i["bought"]))
    for i in data:
        if i["sold"] == None:
            continue
        else:
            price_sold = Decimal(float(i["sold"])) * Decimal(float(i["matecoin_price"]))
            data_sold.append(price_sold)
            account_sold.append(float(i["sold"]))


    matecoin_account = (sum(account_bought) - sum(account_sold))
    earned_money = (sum(data_bought) - sum(data_sold))

    new_data = {
    "earned_money": str(earned_money),
    "matecoin_account": str(matecoin_account)}


    with open("profit.json", "w") as file:
        mentors = json.dump(new_data, file)


calculate_profit()