from django.test import TestCase

from _3caassurance.templatetags._3cassurance_tags import dynamic_trans, first_name, surname


class Product:
    def __init__(self, desc_fr):
        self.desc_fr = desc_fr


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

    def test_should_return_surname_given_a_complete_name(self):
        # GIVEN
        complete_name = 'Abdel Karim Mahat'

        # WHEN
        actual = surname(None, complete_name)

        # THEN
        self.assertEqual(actual, 'Mahat')
