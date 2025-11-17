import json
from decimal import Decimal
from decimal import getcontext
getcontext().prec = 50

def calculate_profit(trades_file="trades.json"):

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    output_filename = "profit.json"

    try:
        with open(trades_file, "r", encoding="utf-8") as f:
            trades = json.load(f)

    except FileNotFoundError:
        print(f"Error: Arquivo não encontrado: {trades_file}")
        return

    except json.JSONDecodeError:
        print(f"Error: O arquivo {trades_file} não é um JSON válido.")
        return
    
    for trade in trades:
        try:
            price = Decimal(trade["matecoin_price"])

            if trade.get("bought"):
                amount = Decimal(trade["bought"])
                matecoin_account += amount
                earned_money -= amount * price

            elif trade.get("sold"):
                amount = Decimal(trade["sold"])
                matecoin_account -= amount
                earned_money += amount * price
        except Exception as e:
            print(f"Error ao processar a trade {trade}: {e}")

    result_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(result_data, f, indent=2)
        print(f"Sucesso! Resultados salvos em {output_filename}")
    except IOError:
        print(f"Error: Não foi possível escrever no arquivo {output_filename}")