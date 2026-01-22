from decimal import Decimal
import json


def calculate_profit(json_info_file: str) -> None:
    money_balance = Decimal("0")
    mate_coin_balance = Decimal("0")

    with (open(json_info_file, "r") as file_read,
          open("profit.json", "w") as file_write):
        json_data = json.load(file_read)

        for decision in json_data:
            if "bought" in decision and decision["bought"]:
                mate_coin_balance += Decimal(decision["bought"])
                money_balance -= (Decimal(decision["bought"])
                                  * Decimal(decision["matecoin_price"]))

            if "sold" in decision and decision["sold"]:
                mate_coin_balance -= Decimal(decision["sold"])
                money_balance += (Decimal(decision["sold"])
                                  * Decimal(decision["matecoin_price"]))

        result_data = {"earned_money": str(money_balance),
                       "matecoin_account": str(mate_coin_balance)}
        json.dump(result_data, file_write, indent=2)
