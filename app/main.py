import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(trades_file: Path) -> None:
    profit = Decimal("0")
    coin_account = Decimal("0")

    with open(trades_file, "r") as trades_file:
        trades_list = json.load(trades_file)

    for dictik in trades_list:
        bought = Decimal("0")
        if dictik["bought"] is not None:
            bought = Decimal(dictik["bought"])

        sold = Decimal("0")
        if dictik["sold"] is not None:
            sold = Decimal(dictik["sold"])

        matecoin_price = Decimal(dictik["matecoin_price"])

        if bought:
            profit -= bought * matecoin_price
        if sold:
            profit += sold * matecoin_price
        mate_coins = bought - sold
        coin_account += mate_coins

    total_trade_result = {
        "earned_money": str(profit),
        "matecoin_account": str(coin_account),
    }
    with open("profit.json", "w") as final_trades_file:
        json.dump(total_trade_result, final_trades_file, indent=2)
