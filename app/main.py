import json
import decimal


def calculate_profit(name: str) -> None:
    result = {
        "earned_money": "",
        "matecoin_account": "",
    }
    bought = 0
    sold = 0
    mc_bought = 0
    mc_sold = 0

    with open(name) as resource:
        trade_data = json.load(resource)
        for trade in trade_data:
            if trade["bought"]:
                bought += decimal.Decimal(
                    trade["bought"]
                ) * decimal.Decimal(
                    trade["matecoin_price"]
                )
                mc_bought += decimal.Decimal(trade["bought"])
            if trade["sold"]:
                sold += decimal.Decimal(
                    trade["sold"]
                ) * decimal.Decimal(
                    trade["matecoin_price"]
                )
                mc_sold += decimal.Decimal(trade["sold"])
        earned_money = -(bought - sold)
        matacoin_account = mc_bought - mc_sold
        result["earned_money"] = str(earned_money)
        result["matecoin_account"] = str(matacoin_account)

    with open("profit.json", "w") as profit:
        json.dump(result, profit, indent=2)
