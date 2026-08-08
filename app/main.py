import json
import decimal


def calculate_profit(file_name: str) -> None:

    def get_safe_decimal(trade_session: dict, key: str) -> decimal.Decimal:
        value = trade_session.get(key, "0")
        if value is None:
            value = "0"
        return decimal.Decimal(str(value))

    with open(file_name) as file, open("profit.json", mode="w") as file_create:
        trade_content = json.load(file)
        earned_money = decimal.Decimal("0")
        matecoins = decimal.Decimal("0")

        for trade_session in trade_content:
            bought = get_safe_decimal(trade_session, "bought")
            sold = get_safe_decimal(trade_session, "sold")
            price = get_safe_decimal(trade_session, "matecoin_price")

            money_spent = bought * price
            money_earned = sold * price

            earned_money += money_earned - money_spent
            matecoins += bought - sold

        trading_result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoins)
        }

        json.dump(trading_result, file_create, indent=2)
