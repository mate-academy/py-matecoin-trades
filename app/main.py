import decimal
import json


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        ready_to_reed = json.load(file)
        total_bought = decimal.Decimal("0")
        total_sold = decimal.Decimal("0")
        all_bought = decimal.Decimal("0")
        all_sold = decimal.Decimal("0")
        for money in ready_to_reed:
            if money["bought"]:
                all_bought += decimal.Decimal(money["bought"])
                total_bought += (decimal.Decimal(money["bought"])
                                 * decimal.Decimal(money["matecoin_price"]))

            if money["sold"]:
                all_sold += decimal.Decimal(money["sold"])
                total_sold += (decimal.Decimal(money["sold"])
                               * decimal.Decimal(money["matecoin_price"]))
        earned_money = total_sold - total_bought
        matecoin_account = all_bought - all_sold
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
