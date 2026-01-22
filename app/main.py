import json
from decimal import Decimal


def calculate_profit(input_file: str) -> str:
    with open(input_file, "r") as json_file:
        data = json.load(json_file)
        bought_matecoin = Decimal("0")
        sold_matecoin = Decimal("0")
        bought_in_dollars = Decimal("0")
        sold_in_dollars = Decimal("0")
        for dic in data:
            if dic["bought"]:
                bought_value = Decimal(str(dic["bought"]))
                currency = Decimal(dic["matecoin_price"])
                bought_matecoin += bought_value
                bought_in_dollars += bought_value * currency
            if dic["sold"]:
                sold_value = Decimal(str(dic["sold"]))
                currency = Decimal(dic["matecoin_price"])
                sold_matecoin += sold_value
                sold_in_dollars += sold_value * currency
        earned_in_dollars = sold_in_dollars - bought_in_dollars
        matecoin_account = bought_matecoin - sold_matecoin
        report = {"earned_money": str(earned_in_dollars),
                  "matecoin_account": str(matecoin_account)}
        with open("profit.json", "w") as f:
            json.dump(report, f, indent=2)
