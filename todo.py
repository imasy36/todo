## Script to implememt ToDO
import argparse
import os
import sqlite3

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
		return 

	def list(self):
		result = self.cur.execute('SELECT *FROM Tasks;')
		for line in result.fetchall():
			print(line)
		return

	def remove(self, data):
		self.cur.execute('DELETE FROM Tasks WHERE id={};'.format(data[0]))
		return

	def changePriority(self, data):
		self.cur.execute('UPDATE Tasks SET priority={} WHERE id={}'.format(data[1],data[0]))
		return


if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Todo CLI tool - to keep your schedules')
	parser.add_argument('--action', nargs=1, type=str, help='command to script add/list/remove/changeStatus')
	parser.add_argument('--priority', nargs=1, type=int, help='priority of task')
	parser.add_argument('--id', nargs=1, type=int, help='Id of the task')
	parser.add_argument('--task', nargs=1, type=str, help='task details')	
	parser.parse_args()
	obj = todo('data','list.sqlite3')

