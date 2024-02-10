import json
from app.main import calculate_profit


def test_calculate_profit(tmp_path):
    # Create a temporary file with test trades data
    trades_data = [
        {"bought": "0.001", "sold": None, "matecoin_price": "50000"},
        {"bought": None, "sold": "0.0005", "matecoin_price": "60000"}
    ]
    trades_file = tmp_path / "test_trades.json"
    with open(trades_file, 'w') as file:
        json.dump(trades_data, file)

    # Call the function with the test file
    calculate_profit(str(trades_file))

    # Load the result from profit.json
    with open("profit.json", 'r') as file:
        result = json.load(file)

    # Assertions for the test
    assert result["earned_money"] == "-25.0"
    assert result["matecoin_account"] == "0.0005"
