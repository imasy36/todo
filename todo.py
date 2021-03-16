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
	parser = argparse.ArgumentParser(prog='ToDo', description='Todo CLI tool - to keep your schedules',
	 epilog='Enjoy your day:-)', fromfile_prefix_chars='@')
	
	parser.add_argument('-a',nargs=1, type=str, help='Add a new task')
	parser.add_argument('-cp', nargs=2, type=int, help='Change priority of task - id, new priority')
	parser.add_argument('-r',nargs=1, type=int, help='Remove a task')
	parser.add_argument('-l', action='store_true', help='list tasks detail')	
	args = parser.parse_args()
	
	obj = todo('data','list.sqlite3')
	print(vars(args))

	if args.l:
		obj.list()

	if args.a:
		obj.add()
	

