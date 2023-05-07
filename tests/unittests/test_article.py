import datetime

from logic.article import Article


class TestArticle:

    article_bbd_date = datetime.date(2023, 5, 22)
    article = Article("Bohnen", 10, article_bbd_date, "Keller")

    # Testing getter functions
    def test_get_article_name(self):
        assert "Bohnen" == self.article.article_name

    def test_get_article_amount(self):
        assert 10 == self.article.article_amount

    def test_get_article_bbd(self):
        assert self.article_bbd_date == self.article.article_bbd

    def test_get_article_storage_location(self):
        assert "Keller" == self.article.article_storage_location

    # Testing setter functions
    def test_set_article_name(self):
        assert "Bohnen" == self.article.article_name
        new_article_name = "Steak"
        self.article.article_name = new_article_name
        assert new_article_name == self.article.article_name

    def test_set_article_amount(self):
        assert 10 == self.article.article_amount
        new_article_amount = 25
        self.article.article_amount = new_article_amount
        assert new_article_amount == self.article.article_amount

    def test_set_article_bbd(self):
        assert self.article_bbd_date == self.article.article_bbd
        new_article_bbd = datetime.date(2023, 5, 25)
        self.article.article_bbd = new_article_bbd
        assert new_article_bbd == self.article.article_bbd

    def test_set_article_storage_location(self):
        assert "Keller" == self.article.article_storage_location
        new_article_storage_location = "Wohnung"
        self.article.article_storage_location = new_article_storage_location
        assert new_article_storage_location == self.article.article_storage_location
