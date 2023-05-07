import datetime


class Article:

    def __init__(self, name, amount=1, bbd=None, storage_location="Wohnung"):
        self.__name = name
        self.__amount = amount
        self.__bbd = bbd
        self.__storage_location = storage_location

    def __str__(self):
        return f"Artikelname: \t{self.__name}\n" \
               f"Menge: \t\t\t{self.__amount}\n" \
               f"MHD: \t\t\t{self.__bbd}\n" \
               f"Lagerort: \t\t{self.__storage_location}"

    @property
    def article_name(self):
        return self.__name

    @property
    def article_amount(self):
        return self.__amount

    @property
    def article_bbd(self):
        return self.__bbd

    @property
    def article_storage_location(self):
        return self.__storage_location

    @article_name.setter
    def article_name(self, value):
        self.__name = value

    @article_amount.setter
    def article_amount(self, value):
        self.__amount = value

    @article_bbd.setter
    def article_bbd(self, value):
        self.__bbd = value

    @article_storage_location.setter
    def article_storage_location(self, value):
        self.__storage_location = value

    def __get_difference_between_dates(self):

        actual_date = datetime.date.today()
        difference = actual_date - self.__bbd

        return difference.days

    def tell_if_product_is_expired(self):

        difference_days = self.__get_difference_between_dates()

        if difference_days == 0:
            print(f"The product expired today.")
        elif difference_days > 0:
            print(f"The product has expired for {difference_days} days.")
        else:
            print(f"The product has a shelf life of {abs(difference_days)} days left.")
