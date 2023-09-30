import decimal
import json


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as file:
        data = json.load(file)

    bought = sum(
        decimal.Decimal(i.get("bought", 0))
        if i.get("bought") is not None
        else decimal.Decimal(0)
        for i in data
    )
    sold = sum(
        decimal.Decimal(i.get("sold", 0))
        if i.get("sold") is not None
        else decimal.Decimal(0)
        for i in data
    )

    bought_matecoin = sum(
        decimal.Decimal(i.get("bought", 0))
        * decimal.Decimal(i.get("matecoin_price", 0))
        if i.get("bought") is not None
        and i.get("matecoin_price") is not None
        else decimal.Decimal(0)
        for i in data
    )

    sold_matecoin = sum(
        decimal.Decimal(i.get("sold", 0))
        * decimal.Decimal(i.get("matecoin_price", 0))
        if i.get("sold") is not None
        and i.get("matecoin_price") is not None
        else decimal.Decimal(0)
        for i in data
    )

    matecoin_account = bought - sold
    earned_money = sold_matecoin - bought_matecoin

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, default=str, indent=2)
