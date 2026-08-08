import json
import decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as infor_fo_coin:
        list_earned_money = []
        list_matecoin_account = []
        need_write = {}
        data = json.load(infor_fo_coin)
    for transaction in data:
        if transaction["bought"] is not None:
            list_earned_money.append(decimal.Decimal(
                str(transaction["bought"])) * -1 * decimal.Decimal(
                str(transaction["matecoin_price"])))
            list_matecoin_account.append(
                decimal.Decimal(str(transaction["bought"])))
        if transaction["sold"] is not None:
            list_earned_money.append(
                decimal.Decimal(
                    str(transaction["sold"]))
                * decimal.Decimal(str(transaction["matecoin_price"])))
            list_matecoin_account.append(
                decimal.Decimal(str(transaction["sold"])) * -1)
    need_write["earned_money"] = str(sum(list_earned_money))
    need_write["matecoin_account"] = str(sum(list_matecoin_account))
    print(need_write)
    with open("profit.json", "w") as file_save:
        json.dump(need_write, file_save, indent=2)
