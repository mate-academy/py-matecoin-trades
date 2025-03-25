import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        content = json.load(file)

    balance = decimal.Decimal(0)
    matecoin_account = decimal.Decimal(0)
    for trade in content:
        matecoin_price = decimal.Decimal(str(trade.get("matecoin_price")))

        coins_bought = decimal.Decimal(str(trade.get("bought", "0") or "0"))
        coins_sold = decimal.Decimal(str(trade.get("sold", "0") or "0"))

        matecoin_account += coins_bought
        matecoin_account -= coins_sold
        balance -= matecoin_price * coins_bought
        balance += matecoin_price * coins_sold

    result = {
        "earned_money": str(balance),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    calculate_profit("app/trades.json")
