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
#
sql = """
    insert into product(name,model_num,model_type) values (
        '새우깡', 'gs25', 'gsitm');
"""

# query 실행하기
cursor.execute(sql)

# commit
db.commit()

# db 연결끊기
db.close()

