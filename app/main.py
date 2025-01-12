import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        json_data = json.load(json_file)
    result = []
    temp_dict = {"earned_money": decimal.Decimal("0.0"),
                 "matecoin_account": decimal.Decimal("0.0")}
    spent = decimal.Decimal("0.0")
    earned = decimal.Decimal("0.0")
    matecoin_account = decimal.Decimal("0.0")
    for coin in json_data:
        if "sold" in coin and coin.get("sold") is not None:
            matecoin_account -= decimal.Decimal(coin.get("sold"))
            earned += (decimal.Decimal(coin.get("matecoin_price"))
                       * decimal.Decimal(coin.get("sold")))
        if coin.get("bought") is not None and "bought" in coin:
            matecoin_account += decimal.Decimal(coin["bought"])
            spent += (decimal.Decimal(coin.get("matecoin_price"))
                      * decimal.Decimal(coin.get("bought")))
    temp_dict["earned_money"] = str(earned - spent)
    temp_dict["matecoin_account"] = str(matecoin_account)
    result.append(temp_dict)
    with open("profit.json", "w+") as result_file:
        json.dump(temp_dict, result_file, indent=2)
