from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Optional, TypedDict, Union


# Define a estrutura/formato de cada trade:
class Trade(TypedDict):
    bought: Optional[str]
    sold: Optional[str]
    matecoin_price: str


# Aqui é que a função pode receber o caminho como string
# ou como um Path:
PathLike = Union[str, Path]


# Aqui convertemos o valor que veio do JSON para Decimal
# Se o valor do JSON for null ou None em python, retorna Decimal("0")
# Porém se o valor for uma string numérica, converte para Decimal:
def _to_decimal(value: Optional[str]) -> Decimal:
    return Decimal("0") if value is None else Decimal(value)


# Aqui iremos converter o Decimal para string no formato decimal "normal"
# para evitar notação científica
def _decimal_to_string(value: Decimal) -> str:
    return format(value, "f")


# Aqui irei ler o arquivo de trades, calcular o lucro/prejuízo
# em dólares, saldo final de mate coin e salvar em profit.json
def calculate_profit(trades_filename: PathLike) -> None:
    getcontext().prec = 50
    # Garanto maior precisão usando até 50 números significativos

    trades_path = Path(trades_filename)
    # Converto str ou Path em Path

    # Abro o arquivo e o leio
    with trades_path.open("r", encoding="utf-8") as file:
        # Aqui transformo o JSON em estruturas nativas do python
        trades = json.load(file)

    earned_money = Decimal("0")
    # Acumulador do lucro/prejuízo em dólares

    matecoin_account = Decimal("0")
    # Acumulador do saldo final de criptomoedas

    # Percorre a cada trade do JSON
    for trade in trades:
        # Converto o preço do dia para Decimal
        price = Decimal(trade["matecoin_price"])

        # Pode retornar uma str numérica ou None
        # (somente se no JSON for null)
        bought = _to_decimal(trade.get("bought"))
        sold = _to_decimal(trade.get("sold"))

        # Atualiza o saldo de moedas
        matecoin_account += bought - sold

        # Atualiza o lucro/prejuízo em dólares
        earned_money += (sold * price) - (bought * price)

    # Aqui monto o JSON de saída no formato esperado,
    # onde valores numéricos precisam estar em formato de str
    result = {
        "earned_money": _decimal_to_string(earned_money),
        "matecoin_account": _decimal_to_string(matecoin_account),
    }

    # Cria ou abre o arquivo profit.json e grava o resultado.
    # O dump escreve o dict em python no formato JSON no arquivo
    with Path("profit.json").open("w", encoding="utf-8") as file:
        json.dump(
            result,
            file,
            ensure_ascii=False,
            indent=2,
        )
