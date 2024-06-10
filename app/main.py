import json
from decimal import Decimal


def calculate_profit(input_file: any = "trades.json",
                     output_file: any = "profit.json") -> None:
    with open(input_file) as f:
        trades_info = json.load(f)

    bought = Decimal("0")
    sold = Decimal("0")
    earned_money = Decimal("0")
    for info in trades_info:
        if info["bought"] is not None:
            bought += Decimal(info["bought"])
            earned_money -= Decimal(info["bought"]) * Decimal(
                info["matecoin_price"])

        if info["sold"] is not None:
            sold += Decimal(info["sold"])
            earned_money += Decimal(info["sold"]) * Decimal(
                info["matecoin_price"])

    matecoin_account = abs(sold - bought)

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(output_file, "w") as f:
        json.dump(profit, f, indent=2)
