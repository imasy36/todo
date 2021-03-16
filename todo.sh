#!/usr/bin/env python3

## Script to implememt ToDO
import argparse
import os
import sqlite3

version = 1.0
class todo:
	def __init__(self, directory, filename):
		self.filename = filename
		self.directory = directory
		if not os.path.isdir(directory):
			os.mkdir(directory)
		self.conn = sqlite3.connect(os.path.join(self.directory, self.filename))
		self.cur = self.conn.cursor()
		self.cur.executescript('''CREATE TABLE IF NOT EXISTS Tasks(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			priority INTEGER DEFAULT 1,
			task TEXT);
			''')

	def menu(self):
		pass

	def add(self, data):
		if len(data)==2:
			self.cur.execute('INSERT INTO Tasks(priority, task) VALUES(?,?);',(data[0], data[1], ))
		else:
			self.cur.execute('INSERT INTO Tasks(task) VALUES(?);',(data[0],))
		self.conn.commit()
		return 

	def list(self):
		result = self.cur.execute('SELECT *FROM Tasks;')
		for line in result.fetchall():
			print(line)
		return

	def remove(self, data):
		self.cur.execute('DELETE FROM Tasks WHERE id={};'.format(data[0]))
		self.conn.commit()
		print('Task with Id:{} deleted successfully'.format(data[0]))
		return

	def changePriority(self, data):
		self.cur.execute('UPDATE Tasks SET priority={} WHERE id={}'.format(data[1],data[0]))
		self.conn.commit()
		return

	def close(self):
		self.conn.commit()
		self.cur.close()

if __name__=='__main__':
	parser = argparse.ArgumentParser(prog='ToDo', description='Todo CLI tool - to keep your schedules',
	 epilog='Enjoy your day:-)', fromfile_prefix_chars='@')
	
	parser.add_argument('-a', '--add', action='store_true', help='Add a task')
	parser.add_argument('-r', '--remove', action='store_true', help='Remove a task')
	parser.add_argument('-cp', '--changePriority', action='store_true', help='Change priority of a task')
	parser.add_argument('-l', '--list', action='store_true', help='list tasks detail')
	parser.add_argument('-ve', '--version', action='store_true', help='version of ToDO')	
	parser.add_argument('vars', nargs='*', help='Additional required details')
	args = parser.parse_args()
	
	obj = todo('data','list.sqlite3')

	if args.version:
		print('ToDo : Version {}\n'.format(version))

	if args.list:
		obj.list()

	if args.add:
		obj.add(args.vars)

	if args.changePriority:
		obj.changePriority(args.vars)

	if args.remove:
		obj.remove(args.vars)

	

