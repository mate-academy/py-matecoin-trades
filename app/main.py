import json
import decimal


def calculate_profit(file_trades: str) -> None:
    with open(file_trades, "r") as file:
        date = json.load(file)
        all_sold = decimal.Decimal("0.0")
        all_bought = decimal.Decimal("0.0")
        all_price_sold = decimal.Decimal("0.0")
        all_price_bought = decimal.Decimal("0.0")
        for day in date:
            if day["sold"] is not None and day["bought"] is None:
                all_sold += decimal.Decimal(day["sold"])
                all_price_sold += decimal.Decimal(day["sold"]) \
                    * decimal.Decimal(day["matecoin_price"])
            elif day["sold"] is None and day["bought"] is not None:
                all_bought += decimal.Decimal(day["bought"])
                all_price_bought += decimal.Decimal(day["bought"]) \
                    * decimal.Decimal(day["matecoin_price"])
            else:
                all_sold += decimal.Decimal(day["sold"])
                all_price_sold += decimal.Decimal(day["sold"]) \
                    * decimal.Decimal(day["matecoin_price"])
                all_bought += decimal.Decimal(day["bought"])
                all_price_bought += decimal.Decimal(day["bought"]) \
                    * decimal.Decimal(day["matecoin_price"])
    with open("profit.json", "w") as file:
        message = {"earned_money": str(all_price_sold - all_price_bought),
                   "matecoin_account": str(all_bought - all_sold)}
        json.dump(message, file, indent=2)
