from utils import get_date, hide_acc, hide_card, hide_transaction, pop_up_msg
import pytest
import json

def test_get_date():
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"


def test_hide_acc():
    assert hide_acc("72731966109147704472") == "**4472"


def test_hide_card():
    assert hide_card("5999414228426353") == "5999 41** **** 6353"


def test_hide_card_negative():
    assert hide_card("59994142284263533") == "Invalid"


def test_hide_transaction():
    assert hide_transaction("Счет 72731966109147704472") == "Счет **4472"


def test_pop_up_msg():
    assert pop_up_msg({
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }) == "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб."
