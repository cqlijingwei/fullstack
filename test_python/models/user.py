import time
from config.db import DB
import sqlite3


def get_user_total():
    with DB() as db:
        cursor = db.cursor()
        sql = f"SELECT count(*) as cnt  FROM `user` where del=0;"
        cursor.execute(sql)
        res = cursor.fetchone()

    return res["cnt"]


def get_user_info(current_page, page_size):
    limit_sql = f" limit {(current_page - 1) * page_size}, {page_size}"
    with DB() as db:
        cursor = db.cursor()
        sql = f"SELECT userid, firstName, lastName, salary FROM `user` where del=0 {limit_sql};"
        cursor.execute(sql)
        res = cursor.fetchall()

    return res


def update_user_info(kwargs):
    userid = kwargs.pop("userid")
    params = []
    sql_mid = ""
    for k, v in kwargs.items():
        if not v:
            continue
        sql_mid += f"`{k}` = ?, "
        params.append(v)
    if not sql_mid:
        return 0
    params.append(userid)
    sql_mid = sql_mid[:-2]
    try:
        with DB() as db:
            cursor = db.cursor()
            sql = f"UPDATE `user` SET {sql_mid} where userid = ? and del=0;"
            cursor.execute(sql, params)
            db.commit()
        return cursor.rowcount
    except sqlite3.IntegrityError:
        print("User repeat")
        return 0

def del_user(userid: int):
    with DB() as db:
        cursor = db.cursor()
        sql = f"UPDATE `user` SET del = 1 where userid = {userid} and del=0;"
        cursor.execute(sql)
        db.commit()
    return cursor.rowcount


def add_user(params: list):
    try:
        with DB() as db:
            cursor = db.cursor()
            sql = "INSERT INTO `user` (firstName, lastName, salary) VALUES (?, ?, ?);"
            cursor.execute(sql, params)
            db.commit()
    except sqlite3.IntegrityError:
        print("User already exists")
        return 0
    return cursor.rowcount
