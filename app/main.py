import json
import decimal


def calculate_profit(name_in: str, name_out: str = "profit.json") -> None:
    with open(name_in) as f:
        money_report = json.load(f)
    total_report = {"earned_money": 0, "matecoin_account": 0}
    for report in money_report:
        if report["bought"] is not None:
            total_report["earned_money"] \
                -= decimal.Decimal(report["matecoin_price"]) \
                * decimal.Decimal(report["bought"])
            total_report["matecoin_account"] \
                += decimal.Decimal(report["bought"])
        if report["sold"] is not None:
            total_report["earned_money"] \
                += decimal.Decimal(report["matecoin_price"])\
                * decimal.Decimal(report["sold"])
            total_report["matecoin_account"] \
                -= decimal.Decimal(report["sold"])

    total_report["earned_money"] = str(total_report["earned_money"])
    total_report["matecoin_account"] = str(total_report["matecoin_account"])

    with open(name_out, "w") as f:
        json.dump(total_report, f, indent=2)
