import json
from decimal import Decimal


def calculate_profit(
    trades_file: str = "trades.json",
    output_file: str = "profit.json",
) -> None:
    # Lê o arquivo JSON com as negociações usando json.load
    with open(trades_file, "r", encoding="utf-8") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        # Se houve compra de moedas
        if trade.get("bought") is not None:
            bought_amount = Decimal(trade["bought"])
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        # Se houve venda de moedas
        if trade.get("sold") is not None:
            sold_amount = Decimal(trade["sold"])
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    # Formata os resultados finais como strings, conforme exigido
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    # Exporta e salva os dados no arquivo profit.json usando json.dump
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
