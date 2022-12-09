from django.test import TestCase

from api.models import Category

class TestModelCategory(TestCase):
    

    def setUp(self):
        
        self.parent_category = Category.objects.create(
                name  = 'Parent',
                description = 'This is the parent category.',
                )

        self.child_category = Category.objects.create(
                name  = 'Child',
                description = 'This is the child category.',
                parent_category=self.parent_category,
                )

    def test_generating_slug(self):

        self.assertEqual(
                self.child_category.slug,
                'parent-child-category'
                )
        self.assertEqual(
                self.parent_category.slug,
                'parent-category'
                )

    def test_gets_all_parents(self):

        parents = self.child_category.get_all_parents()

        self.assertEqual(parents, [self.parent_category])


    def test_gets_all_parents1(self):

        subchild_category = Category.objects.create(
                name  = 'subchild',
                description = 'This is a category.',
                parent_category=self.child_category,
                )

        parents = subchild_category.get_all_parents()

        self.assertEqual(parents, [self.parent_category, self.child_category])








