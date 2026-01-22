import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades = json.load(f)

    trader_account = {
        "earned_money": decimal.Decimal("0"),
        "matecoin_account": decimal.Decimal("0"),
    }
    for trade in trades:
        price = decimal.Decimal(f'{trade["matecoin_price"]}')
        if trade["bought"] is not None:
            buy = decimal.Decimal(f'{trade["bought"]}')
            trader_account["earned_money"] -= buy * price
            trader_account["matecoin_account"] += buy
        if trade["sold"] is not None:
            sell = decimal.Decimal(f'{trade["sold"]}')
            trader_account["earned_money"] += sell * price
            trader_account["matecoin_account"] -= sell

    trader_account_str = {
        "earned_money": str(trader_account["earned_money"]),
        "matecoin_account": str(trader_account["matecoin_account"]),
    }

    with open("profit.json", "w") as f:
        json.dump(trader_account_str, f, indent=2)
