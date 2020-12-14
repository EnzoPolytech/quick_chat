import sqlite3
from os import path

def get_rooms(db_path):
	try:
		connect = sqlite3.connect(db_path)
	
	except sqlite3.OperationalError:
		print('Error in get_rooms(..), wrong path given !')
		return False

	cursor = connect.cursor()

	sql = 'SELECT room_name FROM Rooms;'

	rooms = cursor.execute(sql).fetchall()

	rooms = [room[0] for room in rooms]

	return rooms

def add_room(db_path, room_name, room_type):
	try:
		connect = sqlite3.connect(db_path)
	
	except sqlite3.OperationalError:
		print('Error in add_room(..), wrong path given !')
		return

	cursor = connect.cursor()

	if (type(room_name) != str):
		print('Error in add_room(..), wrong type given for room name !')
		return

	if (type(room_type) != str):
		print('Error in add_room(..), wrong type given for room type !')
		return

	names_list = get_rooms(db_path)

	for name in names_list:
		if name == room_name:
			print('Error in add_room(..), room name already exist !')
			return

	sql = 'INSERT INTO Rooms (room_name,room_type) VALUES (?,?)'

	cursor.execute(sql,(room_name, room_type))
	connect.commit()


def delete_room(db_path, room_name):
	try:
		connect = sqlite3.connect(db_path)
	
	except sqlite3.OperationalError:
		print('Error in delete_room(..), wrong path given ! .. ok\n')
		return

	cursor = connect.cursor()

	sql = 'DELETE FROM Rooms WHERE room_name=?'

	cursor.execute(sql,(room_name,))
	connect.commit()


def get_users(db_path):
	try:
		connect = sqlite3.connect(db_path)
	
	except sqlite3.OperationalError:
		print('Error in get_users(..), wrong path given ! .. ok\n')
		return

	cursor = connect.cursor()

	sql = 'SELECT user_name FROM Users;'

	users = cursor.execute(sql ).fetchall()

	users = [user[0] for user in users]

	return users


def add_user(db_path, user_name, user_role, user_rights, user_password):
	try:
		connect = sqlite3.connect(db_path)
	
	except sqlite3.OperationalError:
		print('Error in add_user(..), wrong path given ! .. ok\n')
		return

	cursor = connect.cursor()

	sql = 'INSERT INTO Users (user_name, user_role, user_rights, user_password) VALUES (?,?,?,?)'

	cursor.execute(sql,(user_name, user_role, user_rights, user_password))
	connect.commit()


def delete_user(db_path, user_name):
	try:
		connect = sqlite3.connect(db_path)
	
	except sqlite3.OperationalError:
		print('Error in delete_user(..), wrong path given ! .. ok\n')
		return

	cursor = connect.cursor()

	sql = 'DELETE FROM Users WHERE user_name=?'

	cursor.execute(sql,(user_name,))
	connect.commit()

def create_db(db_path):
	try:
		connect = sqlite3.connect(db_path)
	
	except sqlite3.OperationalError:
		print('Error in create_db(..), wrong path given ! .. ok\n')
		return

	cursor = connect.cursor()

	cursor.execute('CREATE TABLE Rooms ([id_room] INTEGER PRIMARY KEY,[room_name] text UNIQUE, [room_type] text)')
	cursor.execute('CREATE TABLE Users ([id_user] INTEGER PRIMARY KEY,[user_name] text UNIQUE, [user_role] integer, [user_rights] integer, [user_password] text)')

	connect.commit()


# if not(path.exists('quick_chat.db')):
# 	create_db(db_path)

# add_user('quick_chat.db','yann.c',0,0,'password')
#add_room('~/Bureau/EISE5/test/quick_chat.db','room0','public')

# print(get_users(db_path))
# print(get_rooms(db_path))
# delete_user(db_path,'yann.c')

