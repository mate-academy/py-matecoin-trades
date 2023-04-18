import decimal
import json


def calculate_profit(file_json: json) -> None:
    with open(file_json) as trades_file:
        trades_dict = json.load(trades_file)
    earned_money = 0
    matecoin_account = 0
    for day in trades_dict:
        bought = day["bought"]
        sold = day["sold"]
        matecoin_price = day["matecoin_price"]
        if sold is None:
            matecoin_account += decimal.Decimal(bought)
            earned_money -= \
                decimal.Decimal(bought) * \
                decimal.Decimal(matecoin_price)
        elif bought is None:
            matecoin_account -= decimal.Decimal(sold)
            earned_money += \
                decimal.Decimal(sold) * \
                decimal.Decimal(matecoin_price)
        else:
            matecoin_account += decimal.Decimal(bought)
            matecoin_account -= decimal.Decimal(sold)
            earned_money -= \
                decimal.Decimal(bought) * \
                decimal.Decimal(matecoin_price)
            earned_money += \
                decimal.Decimal(sold) * \
                decimal.Decimal(matecoin_price)
    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as profit_file:
        json.dump(profit_dict, profit_file, indent=2)
