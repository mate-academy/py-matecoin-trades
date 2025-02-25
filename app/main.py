import decimal
import json


def calculate_profit(file_name="trades.json") -> None:
    bought = decimal.Decimal(0)
    sold = decimal.Decimal(0)

    mate_coin_bought = decimal.Decimal(0)
    mate_coin_sold = decimal.Decimal(0)

    with open(file_name, "r") as trade:
        rows = json.load(trade)

    for key in rows:
        if key["bought"] and not isinstance(key["sold"], str):
            dec_key_bought = decimal.Decimal(key["bought"])
            dec_price = decimal.Decimal(key["matecoin_price"])
            bought += dec_key_bought
            mate_coin_bought += (dec_key_bought * dec_price)
        elif key["sold"] and not isinstance(key["bought"], str):
            dec_key_sold = decimal.Decimal(key["sold"])
            dec_price = decimal.Decimal(key["matecoin_price"])
            sold += dec_key_sold
            mate_coin_sold += (dec_key_sold * dec_price)
        else:
            dec_key_bought = decimal.Decimal(key["bought"])
            dec_key_sold = decimal.Decimal(key["sold"])
            bought += dec_key_bought
            sold += dec_key_sold

            dec_price = decimal.Decimal(key["matecoin_price"])
            mate_coin_bought += (dec_key_bought * dec_price)
            mate_coin_sold += (dec_key_sold * dec_price)

    earned_money = decimal.Decimal(bought - sold)
    matecoin_account = decimal.Decimal(mate_coin_sold - mate_coin_bought)

    profit_json = {
        "earned_money": str(matecoin_account),
        "matecoin_account": str(earned_money)
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(profit_json, f, indent=2)
