import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        money_balance = 0
        coin_balance = 0
        trades = json.load(file)
        for trade in trades:
            if trade["bought"] is not None:
                money_balance -= decimal.Decimal(trade["bought"]
                                                 ) * decimal.Decimal(
                    trade["matecoin_price"])
                coin_balance += decimal.Decimal(trade["bought"])
            if trade["sold"]:
                money_balance += decimal.Decimal(trade["sold"]
                                                 ) * decimal.Decimal(
                    trade["matecoin_price"])
                coin_balance -= decimal.Decimal(trade["sold"])
        money_balance = str(money_balance)
        coin_balance = str(coin_balance)
        result = {"earned_money": money_balance,
                  "matecoin_account": coin_balance}
        with open("profit.json", "w") as f:
            json.dump(result, f, indent=2)
