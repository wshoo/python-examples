from pymongo import MongoClient

client = MongoClient()

db = client.pymongo_test # client['pymongo_test'] 选择数据库，如果这个数据库不存的话，会帮你创建
collection = db.posts # db['posts] 选择一个集合，就相当于mysql里面表

post_1 = {
    'title': 'hello',
    'content': 'first',
    'author': 'wang'
}
post_2 = {
    'title': 'hi',
    'content': 'second',
    'author': 'liang'
}
post_3 = {
    'title': 'koniciwa',
    'content': 'third',
    'author': 'liang'
}

new_result = collection.insert_many([post_1, post_2]) # insert_one
print('multiple post: {}'.format(new_result.inserted_ids))

wangs_post = collection.find_one({'author': 'wang'})
print(wangs_post)

liangs_posts = collection.find({'author': 'liang'})
for post in liangs_posts:
    print(post)