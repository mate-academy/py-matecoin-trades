import json
import decimal


def calculate_profit(filename_input: str) -> None:
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    with open(filename_input) as inp:
        content = json.load(inp)

        for dict_info in content:
            if dict_info["bought"] is not None:
                earned_money -= decimal.Decimal(
                    dict_info["bought"]
                ) * decimal.Decimal(
                    dict_info["matecoin_price"]
                )
                matecoin_account += decimal.Decimal(dict_info["bought"])
            if dict_info["sold"] is not None:
                earned_money += decimal.Decimal(
                    dict_info["sold"]
                ) * decimal.Decimal(
                    dict_info["matecoin_price"]
                )
                matecoin_account -= decimal.Decimal(dict_info["sold"])

    result_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as outp:
        json.dump(result_dict, outp, indent=2)
