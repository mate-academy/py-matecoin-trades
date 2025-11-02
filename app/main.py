import json

from decimal import Decimal


def calculate_profit(file_info: str) -> None:
    profit_data = {"earned_money": Decimal("0"),
                   "matecoin_account": Decimal("0")}

    with open(file_info, "r") as jsf:
        data = json.load(jsf)

    for operation in data:
        matecoin_price = Decimal(str(operation["matecoin_price"]))

        bought = operation.get("bought")
        if bought is not None:
            bought = Decimal(str(operation["bought"]))
            profit_data["earned_money"] = (profit_data["earned_money"]
                                           - (bought * matecoin_price))
            profit_data["matecoin_account"] = (profit_data["matecoin_account"]
                                               + bought)

        sold = operation.get("sold")
        if sold is not None:
            sold = Decimal(str(operation["sold"]))
            profit_data["earned_money"] = (profit_data["earned_money"]
                                           + (sold * matecoin_price))
            profit_data["matecoin_account"] = (profit_data["matecoin_account"]
                                               - sold)

    profit = {key: str(val) for key, val in profit_data.items()}

    with open("profit.json", "w") as pjs:
        json.dump(profit, pjs, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
