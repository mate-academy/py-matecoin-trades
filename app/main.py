import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades_list = json.load(f)
        print(trades_list)
    bought = decimal.Decimal("0")
    sold = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for trade in trades_list:
        trade_matecoin_price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            trade_bought = decimal.Decimal(trade["bought"])
            bought = bought + trade_bought * trade_matecoin_price
            matecoin_account = matecoin_account + trade_bought
        if trade["sold"] is not None:
            trade_sold = decimal.Decimal(trade["sold"])
            sold = sold + trade_sold * trade_matecoin_price
            matecoin_account = matecoin_account - trade_sold
    earned = sold - bought
    print("bought:", bought, ", sold:", sold, ", earned:", earned)
    profit = {
        "earned_money": str(earned),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
