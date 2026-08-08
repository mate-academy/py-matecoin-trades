import json
import decimal


def calculate_profit():
    with open("trades.json") as file:
        trades = json.load(file)

    bought = 0
    sold = 0
    earned_money = 0
    matecoin_account = 0

    for deal in trades:
        matecoin_price = decimal.Decimal(deal["matecoin_price"])

        was_bought = deal["bought"]
        was_sold = deal["sold"]

        if was_bought:
            was_bought = decimal.Decimal(was_bought)

            bought += was_bought * matecoin_price
            earned_money -= was_bought * matecoin_price
            matecoin_account += was_bought
            continue

        if was_sold:
            was_sold = decimal.Decimal(was_sold)

            sold += was_sold * matecoin_price
            earned_money += was_sold * matecoin_price
            matecoin_account -= was_sold
            continue

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
