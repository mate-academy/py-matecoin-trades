import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount_bought = Decimal(trade["bought"])
            matecoin_account += amount_bought
            # Comprar gasta dinheiro (valor negativo)
            earned_money -= amount_bought * price

        if trade["sold"] is not None:
            amount_sold = Decimal(trade["sold"])
            matecoin_account -= amount_sold
            # Vender gera dinheiro (valor positivo)
            earned_money += amount_sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file)
