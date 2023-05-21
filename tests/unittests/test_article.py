import datetime

from logic.article import Article


class TestArticle:
    article_bbd_date = datetime.date(2023, 5, 22)
    article = Article("Bohnen", 10, article_bbd_date, "Keller")

    # Testing constructor
    def test_init(self) -> None:
        holds_correct_class = isinstance(self.article, Article)
        has_name = hasattr(self.article, "article_name")
        has_amount = hasattr(self.article, "article_amount")
        has_bbd = hasattr(self.article, "article_bbd")
        has_location = hasattr(self.article, "article_storage_location")

        assert holds_correct_class is True
        assert has_name is True
        assert has_amount is True
        assert has_bbd is True
        assert has_location is True

    # Testing getter functions
    def test_get_article_name(self) -> None:
        assert "Bohnen" == self.article.article_name

    def test_get_article_amount(self) -> None:
        assert 10 == self.article.article_amount

    def test_get_article_bbd(self) -> None:
        assert self.article_bbd_date == self.article.article_bbd

    def test_get_article_storage_location(self) -> None:
        assert "Keller" == self.article.article_storage_location

    # Testing setter functions
    def test_set_article_name(self) -> None:
        assert "Bohnen" == self.article.article_name
        new_article_name = "Steak"
        self.article.article_name = new_article_name
        assert new_article_name == self.article.article_name

    def test_set_article_amount(self) -> None:
        assert 10 == self.article.article_amount
        new_article_amount = 25
        self.article.article_amount = new_article_amount
        assert new_article_amount == self.article.article_amount

    def test_set_article_bbd(self) -> None:
        assert self.article_bbd_date == self.article.article_bbd
        new_article_bbd = datetime.date(2023, 5, 25)
        self.article.article_bbd = new_article_bbd
        assert new_article_bbd == self.article.article_bbd

    def test_set_article_storage_location(self) -> None:
        assert "Keller" == self.article.article_storage_location
        new_article_storage_location = "Wohnung"
        self.article.article_storage_location = new_article_storage_location
        assert new_article_storage_location == self.article.article_storage_location

    # Testing class functions
    def test_tell_if_product_is_expired(self) -> None:

        actual_date = datetime.date(2023, 5, 22)

        expiration_date_today = datetime.date(2023, 5, 22)
        expiration_date_time_over = datetime.date(2023, 2, 10)
        expiration_date_time_left = datetime.date(2024, 5, 17)

        self.article_dummy_one = Article("Joghurt", 3, expiration_date_today, "Vorratsschrank")
        self.article_dummy_two = Article("Schinken", 1, expiration_date_time_over, "Kühlschrank")
        self.article_dummy_three = Article("Getrocknete Tomaten", 5, expiration_date_time_left, "Vorratsschrank")

        difference_days_article_dummy_one = actual_date - self.article_dummy_one.article_bbd
        difference_days_article_dummy_two = actual_date - self.article_dummy_two.article_bbd
        difference_days_article_dummy_three = actual_date - self.article_dummy_three.article_bbd

        difference_days_equals_zero = difference_days_article_dummy_one.days
        difference_days_positive_number = difference_days_article_dummy_two.days
        difference_days_negative_number = difference_days_article_dummy_three.days

        def test_tell_if_product_is_expired(difference_days: int | float) -> str:

            if difference_days == 0:
                return f"The product expired today."
            elif difference_days > 0:
                return f"The product has expired for {difference_days} days."
            else:
                return f"The product has a shelf life of {abs(difference_days)} days left."

        result_one = test_tell_if_product_is_expired(difference_days_equals_zero)
        result_two = test_tell_if_product_is_expired(difference_days_positive_number)
        result_three = test_tell_if_product_is_expired(difference_days_negative_number)

        assert f"The product expired today." in result_one
        assert f"The product has expired for {difference_days_positive_number} days." in result_two
        assert f"The product has a shelf life of {abs(difference_days_negative_number)} days left." in result_three
