import json

from decimal import Decimal


def calculate_profit(file_with_transaction: json) -> Decimal:
    def count_income_from_transaction(transaction: dict) -> Decimal:
        if transaction["sold"] is None:
            return -(Decimal(transaction["bought"])
                     * Decimal(transaction["matecoin_price"]))
        elif transaction["bought"] is None:
            return (Decimal(transaction["sold"])
                    * Decimal(transaction["matecoin_price"]))
        bought_expense = (Decimal(transaction["bought"])
                          * Decimal(transaction["matecoin_price"]))
        sold_income = (Decimal(transaction["sold"])
                       * Decimal(transaction["matecoin_price"]))
        return sold_income - bought_expense

    def count_coin_amount_from_transaction(transaction: dict) -> Decimal:
        if transaction["sold"] is None:
            return Decimal(transaction["bought"])
        elif transaction["bought"] is None:
            return -Decimal(transaction["sold"])
        return Decimal(transaction["bought"]) - Decimal(transaction["sold"])

    earned_money = 0
    matecoin_account = 0
    with open(file_with_transaction, "r") as f:
        transactions = json.load(f)
        for transaction in transactions:
            earned_money += count_income_from_transaction(transaction)
            matecoin_account += count_coin_amount_from_transaction(transaction)

    financial_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as profit:
        json.dump(financial_data, profit, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
