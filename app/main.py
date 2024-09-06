import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    # Читання даних з файлу JSON
    with open(trades_file, "r") as file:
        trades = json.load(file)

    # Ініціалізація змінних для розрахунку прибутку і кількості монет
    dollars_amount = Decimal(0)
    coins_amount = Decimal(0)

    # Обробка кожної операції з JSON
    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade["matecoin_price"])

        # Якщо була покупка
        if bought is not None:
            dollars_amount -= Decimal(bought) * matecoin_price
            coins_amount += Decimal(bought)

        # Якщо був продаж
        if sold is not None:
            dollars_amount += Decimal(sold) * matecoin_price
            coins_amount -= Decimal(sold)

    # Підготовка даних для запису в результат
    result_data = {
        "earned_money": str(dollars_amount),
        "matecoin_account": str(coins_amount)
    }

    # Запис результату в файл JSON
    with open("profit.json", "w") as file:
        json.dump(result_data, file, indent=2)


# Викликаємо функцію з назвою файлу з трейдами
if __name__ == "__main__":
    calculate_profit("trades.json")
