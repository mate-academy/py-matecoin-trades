from app.main import calculate_profit


def test_calculate_profit_runs_without_error() -> None:
    # Просто проверяем, что функция вызывается без ошибок
    # Требуется файл trades.json в корне проекта
    calculate_profit("trades.json")
