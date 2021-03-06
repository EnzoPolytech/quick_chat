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

	# ------------------------ #
	# TEST GET ROOMS FUNCTIONS #
	# ------------------------ #

	def test_get_rooms_connect(self):
		rooms = get_rooms(self.wrong_path)

	def test_get_rooms(self):
		self.assertEqual(get_rooms(self.right_path), [])

	# ----------------------- #
	# TEST ADD ROOM FUNCTIONS #
	# ----------------------- #

	def test_add_room_funct(self):
		# correct add public room
		# self.assertTrue(add_room(self.right_path, 'room0', 'public'))
		add_room(self.right_path, 'room0', 'public')

		# correct add private room (what about right ?)
		self.assertTrue(add_room(self.right_path, 'room1', 'private'))

	def test_add_room_connect(self):
		# test connect wrong path
		self.assertEqual(add_room(self.wrong_path, 'room3', 'public'), -4)

	def test_add_room_name(self):
		# test unique room name
		add_room(self.right_path, 'room0', 'public')
		self.assertEqual(add_room(self.right_path, 'room0', 'public'), -1)

	def test_add_room_type_name(self):
		# test wrong type room name
		self.assertEqual(add_room(self.right_path, 12, 'public'), -3)

	def test_add_room_type_type(self):
		# test wrong type room type
		self.assertEqual(add_room(self.right_path, 'room2', 13), -2)

	# ----------------------- #
	# TEST ADD USER FUNCTIONS #
	# ----------------------- #

	def test_add_user_funct(self):
		# correct add user with role 0 and 0 right
		add_user(self.right_path, 'yann.c', 0, 0, 'password')

		# correct add user with role 1 and 1 right
		add_user(self.right_path, 'enzo.c', 1, 1, 'password')

		# correct add user with role 0 and 1 right (possible ?)
		add_user(self.right_path, 'julie.f', 0, 1, 'password')

	def test_add_user_connect(self):
		# test connect wrong path
		add_user(self.wrong_path, 'charlie.o', 0, 0, 'password')

	def test_add_user_name(self):
		# test unique user name
		add_user(self.right_path, 'yann.c', 0, 0, 'password')

	def test_add_user_type_role(self):
		# test wrong role type
		add_user(self.right_path, 'jean.p', 'hello', 0, 'password')

	def test_add_user_type_right(self):
		# test wrong right type
		add_user(self.right_path, 'paul.j', 0, 'world', 'password')

	def test_add_user_type_password(self):
		# test wrong user password type
		add_user(self.right_path, 'elyoth.h', 0, 0, 12)

	# ------------------------ #
	# TEST GET USERS FUNCTIONS #
	# ------------------------ #

	def test_get_users(self):
		self.assertEqual(get_users(self.right_path), [])

	def tearDown(self):
		# Db remove :
		os.remove("quick_chat.db")

	# ---------------------- #
	# TEST DELETE FUNCTIONS  #
	# ---------------------- #

	def test_delete_room(self):
		# add and delete a room
		add_room(self.right_path, 'room0', 'public')
		delete_room(self.right_path, 'room0')
		self.assertEqual(get_rooms(self.right_path), [])
		# try to delete a room that does not exist
		delete_room(self.right_path, 'room0')

	def test_delete_user(self):
		# check if the room has been deleted
		add_user(self.right_path, 'yann.c', 0, 0, 'password')
		delete_user(self.right_path, 'yann.c')
		self.assertEqual(get_users(self.right_path), [])
		# try to delete a user that does not exist
		delete_user(self.right_path, 'yann.c')


if __name__ == '__main__':

	unittest.main()
