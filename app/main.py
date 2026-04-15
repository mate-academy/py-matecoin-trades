import json
from decimal import Decimal


def calculate_profit(trades_file_path: str) -> None:
    # 1. Leer y cargar los datos
    with open(trades_file_path, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # 2. Procesar cada transacción
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        
        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            # Comprar resta dinero y suma monedas
            earned_money -= bought_volume * price
            matecoin_account += bought_volume
            
        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            # Vender suma dinero y resta monedas
            earned_money += sold_volume * price
            matecoin_account -= sold_volume

    # 3. Preparar el resultado (todo como string según el requisito)
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # 4. Volcar datos en profit.json
    with open("profit.json", "w") as file:
        json.dump(result, file)
