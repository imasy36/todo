## Script to implememt ToDO
import argparse
import os

class todo:
	def __init__(self, filename):
		self.filename = filename

	def add():
		print('add')
		pass

	def list():
		print("list")
		pass

	def remove():
		pass

	def changeStatus():
		pass

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='Todo CLI tool - to keep your schedules')
	parser.add_argument('action', nargs=1, type=str, help='command to script add/list/remove/changeStatus')
	parser.add_argument('additional', nargs='*', type=str, help='Additional input required')
	parser.parse_args()
	
