import json
import decimal


def calculate_profit(file_name: str) -> None:
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    with open(file_name, "r") as trades_json:
        trade = json.load(trades_json)

    for i in trade:
        bought = decimal.Decimal(i["bought"] if i["bought"]
                                 else decimal.Decimal("0"))
        sold = decimal.Decimal(i["sold"] if i["sold"]
                               else decimal.Decimal("0"))
        matecoin_price = decimal.Decimal(i["matecoin_price"]
                                         if i["matecoin_price"]
                                         else decimal.Decimal("0"))
        earned_money += sold * matecoin_price - bought * matecoin_price
        matecoin_account += bought - sold
    profit_str = {"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as profit_json:
        json.dump(profit_str, profit_json, indent=2)
