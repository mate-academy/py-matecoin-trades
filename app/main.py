import json
from decimal import Decimal


def sum_trade_results(trade: str, trades: list) -> Decimal:
    sum_of_trades = sum(
        Decimal(str(trans[trade])) * Decimal(str(trans["matecoin_price"]))
        for trans in trades
        if trans[trade]
    )
    return sum_of_trades


def sum_traded_coins(trade: str, trades: list) -> Decimal:
    traded_coins = sum(
        Decimal(str(trans[trade]))
        for trans in trades
        if trans[trade]
    )
    return traded_coins


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as j_file:
        trades_entries = json.load(j_file)

    bought_coins = Decimal(sum_trade_results("bought", trades_entries))
    sold_coins = Decimal(sum_trade_results("sold", trades_entries))
    amt_bought = Decimal(sum_traded_coins("bought", trades_entries))
    amt_sold = Decimal(sum_traded_coins("sold", trades_entries))
    result_dict = {
        "earned_money": str(sold_coins - bought_coins),
        "matecoin_account": str(amt_bought - amt_sold)
    }
    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)
