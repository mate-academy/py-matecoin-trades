from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    bought, sold = 0, 0
    b_crypto, s_crypto = 0, 0

    with open(file_name, "r") as f:
        transactions = json.load(f)
        t_len = len(transactions)
        for i in range(t_len):
            for value in transactions[i].keys():
                if transactions[i][value] is None:
                    transactions[i][value] = 0

            rate = Decimal(transactions[i]["matecoin_price"])
            b_crypto += Decimal(transactions[i]["bought"])
            bought += Decimal(transactions[i]["bought"]) * rate
            s_crypto += Decimal(transactions[i]["sold"])
            sold += Decimal(transactions[i]["sold"]) * rate

    result = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(b_crypto - s_crypto)
    }

    with (
        open("C:\\Users\\xXx\\PycharmProjects\\py-matecoin-trades\\"
             "profit.json", "w") as f2):
        json.dump(result, f2, indent=2)
