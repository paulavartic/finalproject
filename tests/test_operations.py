from utils import get_date, hide_acc, hide_card, hide_transaction


def test_get_date():
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"


def test_hide_acc():
    assert hide_acc("72731966109147704472") == "**4472"


def test_hide_card():
    assert hide_card("5999414228426353") == "5999 41** **** 6353"


def test_hide_transaction():
    assert hide_transaction("Счет 72731966109147704472") == "Счет **4472"
