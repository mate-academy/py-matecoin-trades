import json

from decimal import Decimal


def calculate_profit(trades_information_file: str) -> None:
    with open(trades_information_file) as trade:
        file_trade = json.load(trade)
    sold_transaction = []
    bought_transaction = []
    for transaction in file_trade:
        matecoin = Decimal(transaction["matecoin_price"])
        if not transaction["sold"] is None:
            sold_transaction.append(
                Decimal(transaction["sold"]) * matecoin)

        if not transaction["bought"] is None:
            bought_transaction.append(
                Decimal(transaction["bought"]) * matecoin)

    matecoin_account_bought = sum(
        Decimal(buy["bought"]) for buy in file_trade
        if not buy["bought"] is None
    )

    matecoin_account_sold = sum(
        Decimal(sol["sold"]) for sol in file_trade
        if not sol["sold"] is None
    )
    earned_money = sum(sold_transaction) - sum(bought_transaction)

    matecoin_account = matecoin_account_bought - matecoin_account_sold
    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    print(profit_dict)
    with open("profit.json", "w") as file_profit:
        json.dump(profit_dict, file_profit, indent=2)
