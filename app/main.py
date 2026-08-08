import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    # Ler o arquivo JSON
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Processar cada trade
    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        # Compra
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        # Venda
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    # Resultado final (valores como string)
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    # Salvar com formatação correta (IMPORTANTE para passar no teste)
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
