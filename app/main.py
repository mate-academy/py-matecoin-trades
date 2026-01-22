import json

import decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as f:
        trades_info = json.load(f)

    account_stats = {
        "earned_money": 0,
        "matecoin_account": 0,
    }

    for i in trades_info:
        if i["bought"]:
            buy_matecoins = (decimal.Decimal(i["matecoin_price"])
                             * decimal.Decimal(i["bought"]))
            account_stats["matecoin_account"] += decimal.Decimal(i["bought"])
            account_stats["earned_money"] -= buy_matecoins
        if i["sold"]:
            sell_matecoins = (decimal.Decimal(i["matecoin_price"])
                              * decimal.Decimal(i["sold"]))
            account_stats["matecoin_account"] -= decimal.Decimal(i["sold"])
            account_stats["earned_money"] += sell_matecoins

    account_stats["matecoin_account"] = str(account_stats["matecoin_account"])
    account_stats["earned_money"] = str(account_stats["earned_money"])

    with open("profit.json", "w") as f:
        json.dump(account_stats, f, indent=2)
