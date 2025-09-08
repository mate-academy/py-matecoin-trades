import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    # Abrir e carregar o arquivo de trades
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            matecoin_account += amount
            earned_money -= amount * price  # gasto para comprar

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            matecoin_account -= amount
            earned_money += amount * price  # recebido pela venda

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    # Salvar no profit.json com indentação
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
