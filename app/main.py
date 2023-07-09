import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file, "r") as trd_file, \
            open("profit.json", "w") as trd_file_w:
        trd_inform = json.load(trd_file)
        ac_inf = {
            "earned_money": Decimal("0"),
            "matecoin_account": Decimal("0")
        }

        for trades in trd_inform:
            if trades["bought"] is not None:
                ac_inf["matecoin_account"] = (ac_inf["matecoin_account"]
                                              + Decimal(trades["bought"]))
                prc_of_b = (Decimal(trades["bought"])
                            * Decimal(trades["matecoin_price"]))
                ac_inf["earned_money"] = ac_inf["earned_money"] - prc_of_b
            if trades["sold"] is not None:
                prc_of_s = \
                    Decimal(trades["sold"]) * Decimal(trades["matecoin_price"])
                ac_inf["earned_money"] = \
                    ac_inf["earned_money"] + prc_of_s
                ac_inf["matecoin_account"] = \
                    ac_inf["matecoin_account"] - Decimal(trades["sold"])

        ac_inf["earned_money"] = str(ac_inf["earned_money"])
        ac_inf["matecoin_account"] = str(ac_inf["matecoin_account"])

        json.dump(ac_inf, trd_file_w, indent=2)
