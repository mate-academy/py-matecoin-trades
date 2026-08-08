from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    loss = 0
    earn = 0
    matecoin = 0
    with open(file_name, "r") as file:
        file_content = json.load(file)
    for trade in file_content:
        if trade.get("bought") is not None:
            loss += (Decimal(trade["bought"])
                     * Decimal(trade["matecoin_price"]))
            matecoin += Decimal(trade["bought"])
        if trade.get("sold") is not None:
            earn += (Decimal(trade["sold"])
                     * Decimal(trade["matecoin_price"]))
            matecoin -= Decimal(trade["sold"])
    earned_money = earn - loss
    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin)
    }
    with open("profit.json", "w") as profit:
        json.dump(profit_dict, profit, indent=2)
