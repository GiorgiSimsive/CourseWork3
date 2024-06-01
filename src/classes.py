from datetime import datetime


class Operation:
    def __init__(self, state, date, amount, currency_name, description, from_, to):
        self.state = state
        self.date = date
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = from_
        self.to = to


    def convert_date(self) -> str:
        """
        Меняет формат даты
         """
        iso_date = datetime.fromisofomat(self.date)
        return iso_date.strftime("%d.%m.%Y")


    def mask_payment_info(self, payment_info):
        """
        Маскирует номер карты и счета
        """
        info = payment_info.split(" ")
        number_card = info.pop(-1)
        if payment_info.startswith("Счет"):
            number_card = number_card + "*"
        else:
            number_card = number_card + "**"
        info.append(number_card)
        return " ".join(info)


    def __lt__(self, other):
        return self.date < other.date


    def __gt__(self, other):
        return self.date > other.date


    def __str__(self):
        return (
            f"{self.convert_date()} {self.description}\n"
            f"{self.mask_payment_info(self.from_)} -> {self.mask_payment_info(self.to)}\n"
            f"{self.amount} {self.currency_name}"
        )