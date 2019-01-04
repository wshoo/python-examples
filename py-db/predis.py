import redis

db = redis.Redis(host='127.0.0.1',port=6379,password='',db=0)

db.set('hi', 'liang')

print(db.get('hi'))
print(db.dbsize())
db.save()
db.flushdb()