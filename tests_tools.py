import sqlite3
import unittest
import os
from quick_tools import *


class TestToolsMethods(unittest.TestCase):

	wrong_path = "~/Dokuments/database.db"
	right_path = "quick_chat.db"

	def setUp(self):
		# Db creation :
		db_path = 'quick_chat.db'
		create_db(db_path)

	def test_connect(self):
		rooms = get_rooms(self.wrong_path)

	def test_add_room(self):
		add_room(self.right_path, 'room0', 'public')

	def test_add_user(self):
		add_user(self.right_path, 'yann.c', 0, 0, 'password')

	def test_get_rooms(self):
		self.assertEqual(get_rooms(self.right_path), [])

	def test_get_users(self):
		self.assertEqual(get_users(self.right_path), [])

	def tearDown(self):
		# Db remove :
		os.remove("quick_chat.db")

if __name__ == '__main__':

	unittest.main()