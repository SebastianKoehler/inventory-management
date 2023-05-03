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
        return self.__name

    @property
    def article_bbd(self):
        return self.__name

    @property
    def article_storage_location(self):
        return self.__name

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
