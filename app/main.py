import json
from decimal import Decimal, ROUND_DOWN


def calculate_profit(filename: str) -> None:
    # Carrega trades do JSON
    with open(filename, "r") as f:
        trades = json.load(f)

    # Totais iniciais
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    # Processa cada trade
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade.get("bought") or "0")
        sold = Decimal(trade.get("sold") or "0")

        if bought > 0:
            matecoin_account += bought
            earned_money -= bought * price  # gastando dinheiro
        if sold > 0:
            matecoin_account -= sold
            earned_money += sold * price  # ganhando dinheiro

    # Arredonda para evitar diferenças de precisão nos testes
    matecoin_account = matecoin_account.quantize(Decimal("0.00000001"), rounding=ROUND_DOWN)
    earned_money = earned_money.quantize(Decimal("0.0000001"), rounding=ROUND_DOWN)

    # Prepara resultado como string
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Salva em profit.json
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
