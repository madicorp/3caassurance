import datetime

from django.test import TestCase

from _3caassurance.templatetags._3cassurance_tags import dynamic_trans, first_name, surname, active_offers


class Product:
    def __init__(self, desc_fr):
        self.desc_fr = desc_fr


class DummyOffer:
    def __init__(self, value=None):
        self.value = value

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False


class TagsTestCase(TestCase):
    def test_should_return_french_description_for_product(self):
        # GIVEN
        product = Product(desc_fr='Description FR')

        # WHEN
        actual = dynamic_trans(None, obj=product, field_name='desc', get_lang_fn=lambda: 'fr')

        # THEN
        self.assertEqual(actual, 'Description FR')

    def test_should_return_french_description_for_dict_product(self):
        # GIVEN
        product = {'desc_fr': 'Description FR'}

        # WHEN
        actual = dynamic_trans(None, obj=product, field_name='desc', get_lang_fn=lambda: 'fr')

        # THEN
        self.assertEqual(actual, 'Description FR')

    def test_should_return_all_first_names_given_a_complete_name(self):
        # GIVEN
        complete_name = 'Abdel Karim Mahat'

        # WHEN
        actual = first_name(None, complete_name)

        # THEN
        self.assertEqual(actual, 'Abdel Karim')

    def test_should_return_surname_given_a_complete_name(self):
        # GIVEN
        complete_name = 'Abdel Karim Mahat'

        # WHEN
        actual = surname(None, complete_name)

        # THEN
        self.assertEqual(actual, 'Mahat')

    def test_should_return_only_active_offers(self):
        # GIVEN
        # 2 active offers and 2 expired
        test_begin_date = datetime.datetime.now()
        one_day_delta = datetime.timedelta(days=1)
        valid_til_tomorrow = TagsTestCase._offer((test_begin_date - one_day_delta).date(),
                                                 (test_begin_date + one_day_delta).date())
        valid_today = TagsTestCase._offer(test_begin_date.date(), test_begin_date.date())
        valid_starting_tomorrow = TagsTestCase._offer((test_begin_date + one_day_delta).date(),
                                                      (test_begin_date + one_day_delta + one_day_delta).date())
        valid_til_yesterday = TagsTestCase._offer((test_begin_date - one_day_delta - one_day_delta).date(),
                                                  (test_begin_date - one_day_delta).date())
        offers = TagsTestCase._offers([valid_til_tomorrow, valid_starting_tomorrow, valid_til_yesterday, valid_today])

        # WHEN
        actual = active_offers(offers)

        # THEN
        self.assertEqual(actual, TagsTestCase._offers([valid_til_tomorrow, valid_today]))

    @staticmethod
    def _offer(start_date, expire_date):
        return {
            'start_date': start_date,
            'expire_date': expire_date
        }

    @staticmethod
    def _offers(offers):
        return map(TagsTestCase._dummy_offer, offers)

    @staticmethod
    def _dummy_offer(offer):
        return DummyOffer(offer)
