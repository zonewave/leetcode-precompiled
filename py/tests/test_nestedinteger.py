from unittest import TestCase

from src.precompiled.nestedinteger import NestedInteger


class TestNestedInteger(TestCase):
    def test_single_integer(self):
        ni = NestedInteger(5)
        self.assertTrue(ni.isInteger())
        self.assertEqual(ni.getInteger(), 5)
        self.assertIsNone(ni.getList())

    def test_nested_list(self):
        ni = NestedInteger([NestedInteger(1), NestedInteger(2)])
        self.assertFalse(ni.isInteger())
        self.assertIsNone(ni.getInteger())
        nested_list = ni.getList()
        self.assertEqual(len(nested_list), 2)
        self.assertTrue(nested_list[0].isInteger())
        self.assertEqual(nested_list[0].getInteger(), 1)
        self.assertTrue(nested_list[1].isInteger())
        self.assertEqual(nested_list[1].getInteger(), 2)

    def test_empty_nested_list(self):
        ni = NestedInteger([])
        self.assertFalse(ni.isInteger())
        self.assertIsNone(ni.getInteger())
        self.assertEqual(ni.getList(), [])
