import json
import decimal


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0

    with open(file_name) as input_file, \
            open("profit.json", "w") as output_file:
        datas = json.load(input_file)

        for data in datas:
            bought = data.get("bought")
            sold = data.get("sold")
            matecoin_price = decimal.Decimal(data.get("matecoin_price"))
            if sold:
                solds = decimal.Decimal(sold)
                earned_money += solds * matecoin_price
                matecoin_account -= solds

            if bought:
                boughts = decimal.Decimal(bought)
                earned_money -= boughts * matecoin_price
                matecoin_account += boughts
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(result, output_file, indent=2)
