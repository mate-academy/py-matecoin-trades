from json import loads
from decimal import *


def calculate_profit(file_name: str) -> None:
    getcontext().prec = 5
    trades = []
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)
    
    with open(file_name) as json_file:
        trades = loads(json_file.read())

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            earned_money -= Decimal(trade["bought"]) * price
            matecoin_account += 
        if trade["sold"]:
            sell = Decimal(trade["sold"])
            
        
