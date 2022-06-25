import json
import decimal


def calculate_profit(file: str):
    with open(file, 'r') as f:
        trade_history = json.load(f)
        profit = 0
        coins = 0
        for deal in trade_history:
            if deal["bought"] is not None:
                bought = decimal.Decimal(deal["bought"])
                matecoin_price = decimal.Decimal(f"{deal['matecoin_price']}")
                profit -= bought * matecoin_price
                coins += bought
            if deal["sold"] is not None:
                sold = decimal.Decimal(deal["sold"])
                matecoin_price = decimal.Decimal(f"{deal['matecoin_price']}")
                profit += sold * matecoin_price
                coins -= sold
    profit_dict = {
        "earned_money": str(profit),
        "matecoin_account": str(coins)
    }
    with open('..\\profit.json', 'w') as f:
        json.dump(profit_dict, f, indent=2)
