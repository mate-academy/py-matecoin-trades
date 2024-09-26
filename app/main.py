import decimal
import json


def calculate_profit(js_file: str) -> None:
    with open(js_file) as f_read, open("profit.json", "w") as f_write:
        profit = decimal.Decimal("0")
        matecoin = decimal.Decimal("0")
        trade = json.load(f_read)
        for deal in trade:
            price_for_matecoin = decimal.Decimal(deal["matecoin_price"])
            if deal["bought"]:
                bought = decimal.Decimal(deal["bought"])
                matecoin += bought
                profit -= bought * price_for_matecoin
            if deal["sold"]:
                sold = decimal.Decimal(deal["sold"])
                matecoin -= sold
                profit += sold * price_for_matecoin
        write_json = {
            "earned_money": str(profit),
            "matecoin_account": str(matecoin)
        }

        json.dump(write_json, f_write, indent=2)
