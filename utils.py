from typing import Any


def organized_operations(data):
    items = [payment for payment in data if payment.get("state") == "EXECUTED"]
    items.sort(key=lambda x: x.get("date"), reverse=True)
    return items


def pop_up_msg(item: dict[str, Any]):
    date = get_date(item.get("date"))
    descr = item.get("description")
    sender = hide_transaction(item.get("from"))
    receiver = hide_transaction(item.get("to"))
    amount = item.get("operationAmount").get("amount")
    currency = item.get("operationAmount").get("currency").get("name")

    if sender:
        sender += " ->"
    else:
        sender = ""

    return f"{date} {descr}\n{sender} {receiver}\n{amount} {currency}"


def get_date(date):
    date_raw = date[0:10].split(sep="-")
    return f"{date_raw[2]}.{date_raw[1]}.{date_raw[0]}"


def hide_acc(number: str):
    if number.isdigit() and len(number) > 4:
        return f"**{number[-4:]}"
    else:
        return "Invalid"


def hide_card(number: str):
    if number.isdigit() and len(number) == 16:
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    else:
        return "Invalid"


def hide_transaction(number):
    if number is None:
        return ""

    message = number.split()

    if message[0] == "Счет":
        hidden_num = hide_acc(message[-1])
    else:
        hidden_num = hide_card(message[-1])

    return ' '.join(message[:-1]) + ' ' + hidden_num




