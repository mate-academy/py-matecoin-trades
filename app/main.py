import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        transactions = json.load(f)

    print(transactions)
    earned_money = 0
    matecoin_account = 0
    for transaction in transactions:
        if transaction["bought"] is not None:
            matecoin_account += decimal.Decimal(transaction["bought"])
            earned_money -= (
                decimal.Decimal(transaction["bought"])
                * decimal.Decimal(transaction["matecoin_price"]))
        if transaction["sold"] is not None:
            matecoin_account -= decimal.Decimal(transaction["sold"])
            earned_money += (
                decimal.Decimal(transaction["sold"])
                * decimal.Decimal(transaction["matecoin_price"]))

    finance_result = {}
    finance_result["earned_money"] = str(earned_money)
    finance_result["matecoin_account"] = str(matecoin_account)
    with open("profit.json", "w") as f:
        json.dump(finance_result, f, indent=2)
