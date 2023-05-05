import datetime

from logic.article import Article


def get_article_name_from_user():
    while True:
        article_name = input("Pleaser enter the name of the new article: ")

        if len(article_name) != 0:
            break
    return article_name


def create_article():
    article_name = get_article_name_from_user()

    article = Article(article_name)

    amount = int(input("Set the amount, otherwise click Enter: "))
    bbd_day = int(input("Set the bbd-day, otherwise click Enter: "))
    bbd_month = int(input("Set the bbd-month, otherwise click Enter: "))
    bbd_year = int(input("Set the bbd-year, otherwise click Enter: "))
    storage_location = input("Set the location, otherwise click Enter: ")

    if amount == 0:
        amount = 1

    if len(storage_location) == 0:
        storage_location = "Wohnung"

    article.article_amount = amount
    article.article_storage_location = storage_location

    if bbd_month == 0 and bbd_year == 0:
        article.article_bbd = datetime.date(datetime.date.today().year, datetime.date.today().month, bbd_day)
    else:
        article.article_bbd = datetime.date(bbd_year, bbd_month, bbd_day)

    return article


def get_difference_between_dates(product_bbd):
    actual_date = datetime.date.today()

    difference = actual_date - product_bbd

    return difference.days


def tell_if_product_is_expired(difference_days):

    if difference_days == 0:
        print(f"The product expired today.")
    elif difference_days > 0:
        print(f"The product has expired for {difference_days} days.")
    else:
        print(f"The product has a shelf life of {abs(difference_days)} days left.")


if __name__ == "__main__":
    var1 = create_article()
    print(var1)

