from datetime import datetime, timedelta

#
# magic number를 쓰지 말자
# =설명없는 특정 상수
DELIVERY_DAYS = 2


def _is_holiday(day: datetime) -> bool:
    return day.weekday() > 5


def get_eta(purchase_date: datetime) -> datetime:
    current_day = purchase_date
    remaining_days = DELIVERY_DAYS

    while remaining_days > 0:
        current_day += timedelta(days=1)
        if not _is_holiday(current_day):
            remaining_days -= 1

    return current_day


def test_get_eta_2023_12_01() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12, 4)


def test_get_eta_2024_12_31() -> None:
    result = get_eta(datetime(2024, 12, 31))
    assert result == datetime(2025, 1, 2)


def test_get_eta_2023_02_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3, 2)


# # 제품 코드
# def add(a: int, b: int) -> int:
#     return a + b

# # 테스트 코드
# def test_add() -> None:
#     # Given
#     a, b = 1, 1

#     # When
#     result = add(a, b)

#     # Then
#     assert result == 2


# def test_simple() -> None:
#     # try:
#     #     1 / 0
#     # except ZeroDivisionError:
#     #     print("Catch!")

#     assert True
