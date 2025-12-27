import unittest

from task_1.src.hash_table import HashTable


class Test_HashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(5)

    def test_insert_and_get(self):
        self.hash_table.insert("key1", "value1")
        self.hash_table.insert("key2", "value2")
        self.assertEqual(self.hash_table.get("key1"), "value1")
        self.assertEqual(self.hash_table.get("key2"), "value2")

    def test_update_value(self):
        self.hash_table.insert("key1", "value1")
        self.hash_table.insert("key1", "value2")
        self.assertEqual(self.hash_table.get("key1"), "value2")

    def test_delete_existing_key(self):
        self.hash_table.insert("key1", "value1")
        result = self.hash_table.delete("key1")
        self.assertTrue(result)
        self.assertIsNone(self.hash_table.get("key1"))

    def test_delete_non_existing_key(self):
        result = self.hash_table.delete("non_existing_key")
        self.assertFalse(result)

    def test_get_non_existing_key(self):
        self.assertIsNone(self.hash_table.get("non_existing_key"))