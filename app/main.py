import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)
    #print(trades)
    capital_usd = Decimal("0")
    coin = Decimal("0")
    for auction in trades:
        if auction["bought"] and not auction["sold"]:
            bought_coin = Decimal(auction["bought"])
            matecoin_price = Decimal(auction["matecoin_price"])
            capital_usd -= bought_coin * matecoin_price
            coin += bought_coin
        elif auction["sold"] and not auction["bought"]:
            sold_coin = Decimal(auction["sold"])
            matecoin_price = Decimal(auction["matecoin_price"])
            capital_usd += sold_coin * matecoin_price
            coin -= sold_coin

    result = [{"earned_money": str(capital_usd), "matecoin_account": str(coin)}]
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)

#calculate_profit("trades.json")