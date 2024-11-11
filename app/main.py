import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    bought_goods, sold_goods, matecoin_account = (
        Decimal(), Decimal(), Decimal()
    )

    profit_json_file = open("profit.json", "w")

    with open(file_name) as trades_json_file:
        for trade in json.load(trades_json_file):
            if trade.get("sold") is not None:
                sold_goods += (
                    Decimal(trade["matecoin_price"]) * Decimal(trade["sold"])
                )
                matecoin_account -= Decimal(trade["sold"])

            if trade.get("bought") is not None:
                bought_goods += (
                    Decimal(trade["matecoin_price"]) * Decimal(trade["bought"])
                )
                matecoin_account += Decimal(trade["bought"])

    json.dump(
        {
            "earned_money": (sold_goods - bought_goods).to_eng_string(),
            "matecoin_account": matecoin_account.to_eng_string()
        },
        profit_json_file,
        indent=2
    )

    profit_json_file.close()
