import os
from pathlib import Path

import inspect
import ast
from unittest import mock

import pytest

from app.main import calculate_profit

BASE_DIR = Path(__file__).resolve().parent.parent

TRADES = f"{BASE_DIR}/app/trades.json"
PROFIT = f"{BASE_DIR}/profit.json"


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.path.exists(self.filename):
            os.remove(self.filename)


def test_function_should_return_none():
    with CleanUpFile(PROFIT):
        assert (
            calculate_profit(TRADES) is None
        ), "Function 'calculate_profit' should return None"


def test_should_not_use_float():
    code = inspect.getsource(calculate_profit)
    parsed_code = ast.parse(code)
    assert "float" not in ast.dump(parsed_code), (
        "You should not use 'float()' inside 'calculate_profit', "
        "because accuracy will be lost."
    )


def test_which_functions_should_be_used():
    code = inspect.getsource(calculate_profit)
    parsed_code = ast.parse(code)

    assert "Decimal" in ast.dump(
        parsed_code
    ), "You should use 'Decimal()' inside 'calculate_profit'"
    assert "open" in ast.dump(
        parsed_code
    ), "You should use 'open()' inside 'calculate_profit'"
    assert "dump" in ast.dump(
        parsed_code
    ), "You should use 'dump()' inside 'calculate_profit'"
    assert "load" in ast.dump(
        parsed_code
    ), "You should use 'load()' inside 'calculate_profit'"
    assert "json" in ast.dump(
        parsed_code
    ), "You should use 'json' module inside 'calculate_profit'"


def test_default_create_profit_file():
    expected = '{\n    "earned_money": "49.8176904",\n    "matecoin_account": "0.00007"\n}'

    with CleanUpFile(PROFIT):
        calculate_profit(TRADES)

        with open(PROFIT) as actual:
            assert actual.read() == expected


@pytest.mark.parametrize(
    "trades, profit",
    [
        pytest.param(
            [
                {"bought": "0.00089", "sold": None, "matecoin_price": "65666.53"},
                {"bought": "0.00029", "sold": "0.00020", "matecoin_price": "65384.28"},
                {"bought": "0.00066", "sold": None, "matecoin_price": "12345.83"},
                {"bought": None, "sold": "0.00070", "matecoin_price": "54321.43"},
            ],
            {"earned_money": "-34.4510437", "matecoin_account": "0.00094"},
        ),
        pytest.param(
            [
                {"bought": "0.00009", "sold": "0.00001", "matecoin_price": "46785.55"},
                {"bought": "0.00007", "sold": "0.00002", "matecoin_price": "93584.28"},
                {"bought": "0.00001", "sold": "0.00009", "matecoin_price": "85345.67"},
                {"bought": "0.00009", "sold": "0.00005", "matecoin_price": "71321.01"},
            ],
            {"earned_money": "-4.4472448", "matecoin_account": "0.00009"},
        ),
    ],
)
@mock.patch("app.main.json.load")
def test_optional_create_profit_file(mock_json_load, trades, profit, monkeypatch):
    with CleanUpFile(PROFIT):
        dump_content = None

        def mocked_dump(content, *args, **kwargs):
            nonlocal dump_content
            dump_content = content

        mock_json_load.return_value = trades
        monkeypatch.setattr("app.main.json.dump", mocked_dump)

        calculate_profit(TRADES)

        assert dump_content == profit
