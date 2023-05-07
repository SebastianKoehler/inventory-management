import datetime

from logic.article import Article


def get_article_name_from_user():

    while True:
        article_name = input("Pleaser enter the name of the new article: ")

        if len(article_name) != 0:
            break

    return article_name


def create_article(article_name, amount, bbd_day, bbd_month, bbd_year, storage_location):

    actual_year = datetime.date.today().year

    try:
        if not isinstance(article_name, str) or \
                str(article_name).isnumeric() or \
                len(str(article_name).strip()) == 0:
            article_name = get_article_name_from_user()

        if amount <= 0:
            amount = 1

        if bbd_day <= 0:
            bbd_day = 1

        if bbd_month <= 0:
            bbd_month = 1

        if bbd_year < (actual_year - 50) or bbd_year > (actual_year + 50):
            bbd_year = datetime.date.today().year

        if not isinstance(storage_location, str) or \
                str(storage_location).isnumeric() or \
                len(str(storage_location).strip()) == 0:
            storage_location = "Wohnung"

        article = Article(article_name)
        article.article_amount = amount

        article.article_bbd = datetime.date(bbd_year, bbd_month, bbd_day)

        article.article_storage_location = storage_location

        return article

    except ValueError:
        return f"Error occurred! Wrong date!"
    except TypeError:
        return f"Error occurred! Amount and dates requiring an integer, not string or else."


if __name__ == "__main__":

    object_properties_1 = {"article_name": "Thunfisch",
                           "amount": 3,
                           "bbd_day": 6,
                           "bbd_month": 5,
                           "bbd_year": 2023,
                           "storage_location": "Kammer"}

    article_1 = create_article(**object_properties_1)

    article_1.tell_if_product_is_expired()
