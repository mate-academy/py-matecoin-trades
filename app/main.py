import json
import decimal


def calculate_profit(json_file_name: str) -> None:
    with open(json_file_name, "r") as f:
        matecoin_data = json.load(f)

        earned_money = decimal.Decimal("0")
        matecoin_account = decimal.Decimal("0")
        for action in matecoin_data:
            if action["bought"] is not None:
                matecoin_account += decimal.Decimal(action["bought"])
                earned_money -= (decimal.Decimal(action["bought"])
                                 * decimal.Decimal(action["matecoin_price"]))
            if action["sold"] is not None:
                matecoin_account -= decimal.Decimal(action["sold"])
                earned_money += (decimal.Decimal(action["sold"])
                                 * decimal.Decimal(action["matecoin_price"]))
    # print(earned_money)
    # print(matecoin_account)

    with open("profit.json", "w") as f:
        json.dump({"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)},
                  f,
                  indent=2)
