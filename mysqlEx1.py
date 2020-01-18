import pymysql

# DB 접속하기.
db = pymsql.connect(host='localhost', port=3306, user='root', passwd="9755", db='mkyu', charset='utf8')



# Cursor 가져오기
cursor = db.cursor()

# SQL query 작성
sql = """
    create table fetish (
        id int unsigned not null auto_increment,
        name varchar(10) not null,
        model_num varchar(20) not null,
        model_type varchar(10) not null,
        primary key(id)
        );
"""

# query 실행하기
cursor.execute(sql)

# commit
db.commit()

# db 연결끊기
db.close()

