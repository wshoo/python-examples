import os

path = r"C:\Users\Administrator\Desktop\cahe\1.txt"
with open(path, 'r') as f:
    dirs = f.readlines()
    for dir in dirs:
        dir = dir.strip()
        os.makedirs('./{}'.format(dir), exist_ok=True)