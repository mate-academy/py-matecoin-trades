from decimal import Decimal, localcontext, ROUND_HALF_EVEN
import json
import os


def to_decimal(value: object) -> Decimal:
    if value is None or value == "":
        return Decimal("0")
    return Decimal(str(value))


def calculate_profit(file_name: str) -> None:
    if not file_name.endswith(".json"):
        raise ValueError("JSON file required")

    if not os.path.exists(file_name):
        raise FileNotFoundError("File not found")

    with open(file_name, "r", encoding="utf-8") as file:
        trades = json.load(file)

    with localcontext() as ctx:
        ctx.prec = 28
        ctx.rounding = ROUND_HALF_EVEN

        total_bought = Decimal("0")
        total_sold = Decimal("0")
        total_profit = Decimal("0")

        for trade in trades:
            bought = to_decimal(trade.get("bought", 0))
            sold = to_decimal(trade.get("sold", 0))
            price = to_decimal(trade.get("matecoin_price", 0))

            total_bought += bought
            total_sold += sold
            total_profit += (sold - bought) * price

        output = {
            "earned_money": str(total_profit),
            "matecoin_account": str(total_bought - total_sold),
        }
        output_path = "profit.json"
        with open(output_path, "w", encoding="utf-8") as output_file:
            json.dump(output, output_file, indent=2)


calculate_profit("app/trades.json")
