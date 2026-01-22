from decimal import Decimal
import json


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as data_json:
        trades = json.load(data_json)

    list_of_bought = []
    list_of_sold = []
    list_of_earned_money = []
    for trade in trades:
        if trade["bought"]:
            list_of_bought.append(Decimal(trade["bought"]))

        if trade["sold"]:
            list_of_sold.append(Decimal(trade["sold"]))
    for trade in trades:
        if trade["bought"] is None:
            trade["bought"] = Decimal(0)
        elif trade["sold"] is None:
            trade["sold"] = Decimal(0)
        elif trade["bought"] and trade["sold"] is None:
            trade["bought"] = Decimal(0)
            trade["sold"] = Decimal(0)
        sold = Decimal(trade["sold"])
        bought = Decimal(trade["bought"])
        matecoin_price = Decimal(trade["matecoin_price"])

        earned_money = (sold - bought) * matecoin_price
        list_of_earned_money.append(earned_money)

    matecoin_account_summary = abs((sum(list_of_sold)) - (sum(list_of_bought)))
    decimal_matecoin = matecoin_account_summary
    profit_data = {
        "earned_money": str(sum(list_of_earned_money)),
        "matecoin_account": str(decimal_matecoin)
    }

    with open("profit.json", "w") as file_result:
        json.dump(profit_data, file_result, indent=2)
