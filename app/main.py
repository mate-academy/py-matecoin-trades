import json
import decimal
import os


def calculate_profit(file: str = f"{os.getcwd()}\\trades.json") -> None:
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    with open(file, "r") as file:
        trade_info = json.load(file)

    for deal in trade_info:

        matecoin_price = decimal.Decimal(deal["matecoin_price"])

        try:
            # buy
            bought = decimal.Decimal(deal["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        except TypeError:
            pass

        try:
            # sale
            sold = decimal.Decimal(deal["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price
        except TypeError:
            pass

    print(f"money:{earned_money}, mate-coins:{matecoin_account}")
    result = ({"earned_money": str(earned_money),
               "matecoin_account": str(matecoin_account)})

    print(f"{os.getcwd()}\profit.json")
    save_path = f"C:\\Users\\hryny\\ma\\py-matecoin-trades/profit.json"
    with open(save_path, "w") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    calculate_profit()
