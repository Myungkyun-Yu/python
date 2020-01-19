import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd="9755", db='mkyu', charset='utf8')

# Cursor 가져오기
cursor = db.cursor()

# SQL query 작성
# sql = """
#     create table product (
#         id int unsigned not null auto_increment,
#         name varchar(10) not null,
#         model_num varchar(20) not null,
#         model_type varchar(10) not null,
#         primary key(id)
#         );
# """

# for 문을 이용하여 database 에 데이터 insert 하기.
for index in range(10):
    product_code = 10001 + index + 1
    sql = """ insert into product values (
        '""" + str(product_code) + """', '새우깡', 'gs25', '농심')""";
    cursor.execute(sql)

# commit
db.commit()

# db 연결끊기
db.close()

