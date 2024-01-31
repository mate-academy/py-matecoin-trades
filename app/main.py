import json
import decimal


def calculate_profit(name: str):
    with open(name) as file_in:
        trades = json.load(file_in)

    bought = decimal.Decimal("0")
    sold = decimal.Decimal("0")
    dollars_spent = decimal.Decimal("0")
    dollars_earnd = decimal.Decimal("0")

    for transaction in trades:

        if transaction["sold"] is None:
            dollars_spent += decimal.Decimal(transaction["bought"]) * decimal\
                .Decimal(transaction["matecoin_price"])
            bought += decimal.Decimal(transaction["bought"])

        if transaction["bought"] is None:
            dollars_earnd += decimal.Decimal(transaction["sold"]) * decimal\
                .Decimal(transaction["matecoin_price"])
            sold += decimal.Decimal(transaction["sold"])

        if transaction["bought"] is not None \
                and transaction["sold"] is not None:

            dollars_spent += decimal.Decimal(transaction["bought"]) * decimal\
                .Decimal(transaction["matecoin_price"])
            bought += decimal.Decimal(transaction["bought"])

            dollars_earnd += decimal.Decimal(transaction["sold"]) * decimal\
                .Decimal(transaction["matecoin_price"])
            sold += decimal.Decimal(transaction["sold"])

    profit = {
        "earned_money": str(dollars_earnd - dollars_spent),
        "matecoin_account": str(bought - sold)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
