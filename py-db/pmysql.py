import pymysql


def my_db(host,user,passwd,db,sql,port=3306,charset='utf8'):
    coon = pymysql.connect(host=host,
                          user=user,
                          password=passwd,
                          db=db,
                          port=port,
                          charset=charset,
                          autocommit=True)

    cur = coon.cursor()   #建立游标
    sql=sql.strip()
    cur.execute(sql)   #执行sql语句，但不会返回执行的结果
    sql_start = sql[:6].lower()#取sql的开头,转成小写
    if sql_start.startswith('select') or sql_start.startswith('show'):
        data = cur.fetchall()  #获取到查询的所有结果
    else:
        data = 'ok'
    cur.close()  #关闭游标
    coon.close()  #关闭连接
    return data

if __name__ == "__main__":

    sql = "insert into myapp_book (book_name,add_time) values ('hello world', now());"
    result = my_db(host='127.0.0.1',user='root',passwd='root',db='yy',sql=sql)
    print(result)


