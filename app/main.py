import json
import decimal
from pathlib import Path


def calculate_profit(file_name: str) -> None:
    temp_value = 0
    money_spent = 0
    received_money = 0
    with open(file_name, "r") as file:
        users_data = json.load(file)

        for user_action in users_data:
            # user_action = json.loads(action)
            if user_action["sold"] is None:
                temp_value += decimal.Decimal(user_action["bought"])
                money_spent += decimal.Decimal(user_action["bought"])\
                    * decimal.Decimal(user_action["matecoin_price"])
            if user_action["bought"] is None:
                temp_value -= decimal.Decimal(user_action["sold"])
                received_money += decimal.Decimal(user_action["sold"]) \
                    * decimal.Decimal(user_action["matecoin_price"])
            if user_action["sold"] is not None \
                    and user_action["bought"] is not None:
                temp_value += decimal.Decimal(user_action["bought"])
                money_spent += decimal.Decimal(user_action["bought"]) \
                    * decimal.Decimal(user_action["matecoin_price"])
                temp_value -= decimal.Decimal(user_action["sold"])
                received_money += decimal.Decimal(user_action["sold"]) \
                    * decimal.Decimal(user_action["matecoin_price"])

    result = {
        "earned_money": str(received_money - money_spent),
        "matecoin_account": str(temp_value)
    }
    base_dir = Path(__file__).resolve().parent.parent
    profit = f"{base_dir}/profit.json"
    with open(profit, "w") as file:
        json.dump(result, file, indent=2)
