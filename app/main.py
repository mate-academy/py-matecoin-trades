import json
from decimal import Decimal
from typing import TypedDict, cast


class Trade(TypedDict):
    bought: str | None
    sold: str | None
    matecoin_price: str


def calculate_profit(trades_path: str) -> None:
    with open(trades_path, "r") as f:
        trades = cast(list[Trade], json.load(f))

    cash_flow: Decimal = Decimal("0")
    matecoin_account: Decimal = Decimal("0")

    for trade in trades:
        price: Decimal = Decimal(trade["matecoin_price"])
        bought: Decimal = Decimal(trade["bought"] or "0")
        sold: Decimal = Decimal(trade["sold"] or "0")

        cash_flow += sold * price - bought * price
        matecoin_account += bought - sold

    result: dict[str, str] = {
        "earned_money": str(cash_flow),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
