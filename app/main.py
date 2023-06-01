import decimal
import json


def calculate_profit(source: str) -> None:
    balance = {
        "earned_money": decimal.Decimal("0"),
        "wasted_money": decimal.Decimal("0"),
        "matecoin_account": decimal.Decimal("0")
    }

    with open(source, "r") as source_json:  # load data
        trading_data = json.load(source_json)

    for transaction in trading_data:  # data -> balance
        if transaction["bought"]:
            balance["wasted_money"] += (decimal.Decimal(transaction["bought"])
                                        * decimal.Decimal(transaction
                                                          ["matecoin_price"]))
            balance["matecoin_account"] += decimal.Decimal(transaction
                                                           ["bought"])

        if transaction["sold"]:
            balance["earned_money"] += (decimal.Decimal(transaction["sold"])
                                        * decimal.Decimal(transaction
                                                          ["matecoin_price"]))

            balance["matecoin_account"] -= decimal.Decimal(transaction["sold"])

        with open("profit.json", "w") as target:  # balance -> result
            data = {
                "earned_money": str(balance["earned_money"]
                                    - balance["wasted_money"]),
                "matecoin_account": str(balance["matecoin_account"])}

            json.dump(data, target, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
