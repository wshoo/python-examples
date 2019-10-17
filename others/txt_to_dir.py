import os

with open('list.txt', 'r') as f:
	dirs = f.readlines()
	for dir in dirs:
		dir = dir.strip()
		os.makedirs('./oa/{}'.format(dir.split()[0]))