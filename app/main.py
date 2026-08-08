import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        bought_trade = trade["bought"]
        sold_trade = trade["sold"]
        matecoin_price = trade["matecoin_price"]
        if bought_trade is not None and sold_trade is None:
            cost = Decimal(bought_trade) * Decimal(matecoin_price)
            earned_money -= cost
            matecoin_account += Decimal(bought_trade)

        elif sold_trade is not None and bought_trade is None:
            revenue = Decimal(sold_trade) * Decimal(matecoin_price)
            earned_money += revenue
            matecoin_account -= Decimal(sold_trade)

        elif sold_trade is not None and bought_trade is not None:
            trade_volume1 = Decimal(sold_trade) * Decimal(matecoin_price)
            trade_volume2 = Decimal(bought_trade) * Decimal(matecoin_price)
            total_volume = trade_volume1 - trade_volume2
            earned_money += total_volume
            matecoin_account += Decimal(bought_trade) - Decimal(sold_trade)

    result_data = {
        "earned_money": str(Decimal(earned_money)),
        "matecoin_account": str(Decimal(matecoin_account))
    }

    with open("profit.json", "w") as output_file:
        json.dump(result_data, output_file, indent=2)
