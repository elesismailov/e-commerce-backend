from django.test import TestCase

from api.helpers.generate_slug import generate_slug

class TestGenerateSlug(TestCase):
    

    def test_generating_slug(self):

        string = 'Nike Air Force 1 LVT'

        slug = generate_slug(string)

        self.assertEqual(
                slug, 
                'nike-air-force-1-lvt'
                )

    def test_taking_several_args(self):

        s1 = 'nike'
        s2 = 'Air Force 1'
        s3 = 'Custom Logo'
        s4 = '12klj2efni12'

        slug = generate_slug(s1, s2, s3, s4)

        self.assertEqual(
                slug,
                'nike-air-force-1-custom-logo-12klj2efni12'
                )

    def test_passing_integer(self):

        s1 = 'nike'

        integer = 123

        slug = generate_slug(s1, integer)

        self.assertEqual(slug, 'nike-123')


    def test_integer_array(self):

        s1 = 'String'

        array = [12,34,56]

        slug = generate_slug(s1, array)

        self.assertEqual(slug, 'string-12-34-56')
        

    def test_passing_dict(self):

        s1 = 'converse'

        d = {'All Star': True}

        slug = generate_slug(s1, d)

        self.assertEqual(slug,
                'converse-all-star-true')



