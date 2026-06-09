import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    # 1. Lecture et conversion du fichier JSON d'entrée
    with open(filename, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # 2. Calcul du solde et des gains de manière précise
    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))

        # Si c'est un achat (bought n'est pas nul)
        if trade.get("bought") is not None:
            bought_amount = Decimal(str(trade["bought"]))
            matecoin_account += bought_amount
            # Acheter diminue l'argent en dollars (earned_money)
            earned_money -= bought_amount * price

        # Si c'est une vente (sold n'est pas nul)
        if trade.get("sold") is not None:
            sold_amount = Decimal(str(trade["sold"]))
            matecoin_account -= sold_amount
            # Vendre augmente l'argent en dollars (earned_money)
            earned_money += sold_amount * price

    # 3. Préparation du dictionnaire final (valeurs converties en chaînes)
    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # 4. Exportation et enregistrement dans profit.json
    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(profit_data, file, indent=2)
