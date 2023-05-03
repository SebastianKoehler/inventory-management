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

    amount = input("Set the amount, otherwise click Enter: ")
    bbd = input("Set the bbd, otherwise click Enter: ")
    storage_location = input("Set the location, otherwise click Enter: ")

    if len(amount) == 0:
        amount = str(1)

    if len(bbd) == 0:
        bbd = "Nicht angegeben"

    if len(storage_location) == 0:
        storage_location = "Wohnung"

    article.article_amount = amount
    article.article_bbd = bbd
    article.article_storage_location = storage_location

    return article


if __name__ == "__main__":
    var1 = create_article()

    print(var1)
