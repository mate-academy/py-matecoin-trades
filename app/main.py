import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    input_file: list[dict] = json.load(open(name, "r"))
    matecoins = Decimal("0")
    buy = Decimal("0")
    sold = Decimal("0")
    for element in input_file:
        if element.get("bought") is not None:
            buy += (Decimal(element.get("bought"))
                    * Decimal(element.get("matecoin_price")))
            matecoins += Decimal(element.get("bought"))
        if element.get("sold") is not None:
            sold += (Decimal(element.get("sold"))
                     * Decimal(element.get("matecoin_price")))
            matecoins -= Decimal(element.get("sold"))
    print(sold - buy)
    print(matecoins)
    out = {"earned_money": f"{sold - buy}", "matecoin_account": f"{matecoins}"}
    json.dump(out, open("profit.json", "w"), indent=2)
