import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    # Читаємо дані з файлу
    with open(filename, "r") as f:
        trades = json.load(f)

    # Обробка кожної угоди
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"]) if trade.get("bought") else Decimal("0")
        sold = Decimal(trade["sold"]) if trade.get("sold") else Decimal("0")

        # Поточний баланс монет
        matecoin_account += bought - sold

        # Прибуток = гроші від продажу - витрати на купівлю
        earned_money += (sold - bought) * price

    # Запис результату у profit.json
    with open("profit.json", "w") as f:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            f,
            indent=2
        )
