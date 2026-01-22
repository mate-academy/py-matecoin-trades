import json

from decimal import Decimal


def calculate_profit(trades_file_name: str = "trades.json") -> None:
    with open(trades_file_name, "r") as json_file:
        trades_data = json.load(json_file)

        earned = 0
        coin_amount = Decimal("0.0")
        for deal in trades_data:
            if deal["bought"]:
                earned -= (
                    Decimal(deal["matecoin_price"]) * Decimal(deal["bought"])
                )
                coin_amount += Decimal(deal["bought"])
            if deal["sold"]:
                earned += (
                    Decimal(deal["matecoin_price"]) * Decimal(deal["sold"])
                )
                coin_amount -= Decimal(deal["sold"])

        def write_profit(profit: dict) -> None:  # cant move up, cause of tests
            with open("profit.json", "w") as profit_file:
                json.dump(profit, profit_file, indent=2)

        write_profit(
            {"earned_money": str(earned), "matecoin_account": str(coin_amount)}
        )


if __name__ == "__main__":
    calculate_profit()
