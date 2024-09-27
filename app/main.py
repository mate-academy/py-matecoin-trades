from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with (open(file_name, "r") as imported,
          open("profit.json", "w") as exported):
        import_data = json.load(imported)
        earned_money = 0
        matecoin_account = 0
        for i in import_data:
            for key, value in i.items():
                if key == "bought" and value is not None:
                    earned_money -= (Decimal(value)
                                     * Decimal(i["matecoin_price"]))
                    matecoin_account += Decimal(value)
                elif key == "sold" and value is not None:
                    earned_money += (Decimal(value)
                                     * Decimal(i["matecoin_price"]))
                    matecoin_account -= Decimal(value)
        coin_trade = {
            "earned_money": f"{earned_money}",
            "matecoin_account": f"{matecoin_account}"
        }
        json.dump(coin_trade, exported, indent=2)
