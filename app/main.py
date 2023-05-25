import decimal
import json


def calculate_profit(name_of_file: str) -> None:
    count_of_coins = decimal.Decimal("0.0")
    count_of_dollars = decimal.Decimal("0.0")
    with open(name_of_file) as f:
        trade_data = json.load(f)
        for trade in trade_data:
            if trade["sold"] is None:
                count_of_coins += decimal.Decimal(trade["bought"])
                count_of_dollars -= decimal.Decimal(
                    trade["matecoin_price"]
                ) * decimal.Decimal(trade["bought"])
            elif trade["bought"] is None:
                count_of_coins -= decimal.Decimal(trade["sold"])
                count_of_dollars += decimal.Decimal(
                    trade["matecoin_price"]
                ) * decimal.Decimal(trade["sold"])
            else:
                count_of_coins += decimal.Decimal(trade["bought"])
                count_of_dollars -= decimal.Decimal(
                    trade["matecoin_price"]
                ) * decimal.Decimal(trade["bought"])
                count_of_coins -= decimal.Decimal(trade["sold"])
                count_of_dollars += decimal.Decimal(
                    trade["matecoin_price"]
                ) * decimal.Decimal(trade["sold"])

    count_of_dollars = str(count_of_dollars)
    count_of_coins = str(count_of_coins)

    result_trade = {
        "earned_money": count_of_dollars,
        "matecoin_account": count_of_coins,
    }

    with open("profit.json", "w") as f:
        json.dump(result_trade, f, indent=2)
