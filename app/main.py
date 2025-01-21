import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    try:
        with open(file_name, "r") as file:
            trades = json.load(file)
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
        return
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


#если указать путь к файлу 'trades.json' или 'app/trades.json' - получаем ошибку 'Error: File trades.json not found'
calculate_profit(
    "c:/Users/Admin/github-projects/py-matecoin-trades/app/trades.json"
)
