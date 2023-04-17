# Matecoin trades

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

You have made some trades with the new cryptocurrency "Matecoin".
In order to calculate profit you loaded json-file `trades.json` with 
trades description. Content of that file is `list of JavaScript Objects`,
`js objects` very similar to 
python `dict`, where keys are  `"bought"` - volume of coins, 
if you bought, 
`"sold"` - volume of coins, if you sold and `matecoin_price` -
price for 1 Matecoin in dollars that day.

Example:
```javascript
// trades.json
[
  {
    "bought": "0.00111",
    "sold": null,
    "matecoin_price": "48911.23"
  },
  {
    "bought": null,
    "sold": "0.00058",
    "matecoin_price": "77830.83"
  }
]
```

Write `calculate_profit` function, which takes the name of the file with
trades information, converts inside data into python native data
structure, counts money profit in dollars and current coin account, dumps
that information in json and saves
in file `profit.json`
```javascript
// profit.json
{
  "earned_money": "-9.1495839",
  "matecoin_account": "0.00053"
}
```
Use should use `Decimal` instead of `float` here, because `float`
do not provide sufficient accuracy for monetary transactions.
All numbers in json should be presented in string format.

**IMPORTANT**: use `load` and `dump` methods for write/read.