import json


from decimal import Decimal


def calculate_profit(new_file: str) -> None:
    with open(new_file) as file_name:
        file_name = json.load(file_name)
        bought = 0
        sold = 0
        coin_account = 0

        for trad in file_name:
            if type(trad["bought"]) == str:
                coin_account += Decimal(trad["bought"])
                bought +=\
                    Decimal(trad["bought"]) * Decimal(trad["matecoin_price"])
            if type(trad["sold"]) == str:
                coin_account -= Decimal(trad["sold"])
                sold += Decimal(trad["sold"]) * Decimal(trad["matecoin_price"])

        earned_money = sold - bought

    date_file = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{coin_account}"
    }
    with open("profit.json", "w") as new_data:
        json.dump(date_file, new_data, indent=2)
