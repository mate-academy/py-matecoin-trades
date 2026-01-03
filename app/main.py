import json
from decimal import Decimal
import os


def calculate_profit(trades_file_name: str) -> dict[str, str]:
    with open(trades_file_name, "r") as file:
        trades_data = json.load(file)

    m_sold = Decimal(0)
    m_bought = Decimal(0)
    coin_sold = Decimal(0)
    coin_bought = Decimal(0)

    for trade in trades_data:
        sold = trade.get("sold")
        bought = trade.get("bought")

        if sold is not None:
            m_sold += Decimal(sold) * Decimal(trade["matecoin_price"])
            coin_sold += Decimal(sold)
        if bought is not None:
            m_bought += Decimal(bought) * Decimal(trade["matecoin_price"])
            coin_bought += Decimal(bought)

    earned_money = m_sold - m_bought
    matecoin_account = coin_bought - coin_sold

    profit_data = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}

    current_dir = os.path.dirname(os.path.abspath(__file__))
    profit_file_path = os.path.join(current_dir, "../profit.json")

    with open(profit_file_path, "w") as file:
        json.dump(profit_data, file, indent=2)

    return None
