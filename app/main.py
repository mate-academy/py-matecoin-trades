import json
import decimal
import os


def calculate_profit(j_file: str = f"{os.getcwd()}\\trades.json") -> None:
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    with open(j_file, "r") as j_file:
        trade_info = json.load(j_file)

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

    print(f"{os.getcwd()}\\profit.json")
    save_path = "C:\\Users\\hryny\\ma\\py-matecoin-trades\\app\\profit.json"
    with open(save_path, "w") as j_file:
        json.dump(result, j_file, indent=2)


if __name__ == "__main__":
    calculate_profit()
