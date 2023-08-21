import os

"""
{
  "employees": [
    {
      "firstName": "Lewis",
      "lastName": "Burson",
      "salary": 40700
    },
    {
      "firstName": "Ian",
      "lastName": "Malcolm",
      "salary": 70000
    },
    {
      "firstName": "Ellie",
      "lastName": "Sattler",
      "salary": 102000
    },
    {
      "firstName": "Dennis",
      "lastName": "Nedry",
      "salary": 52000
    },
    {
      "firstName": "John",
      "lastName": "Hammond",
      "salary": 89600
    },
    {
      "firstName": "Ray",
      "lastName": "Arnold",
      "salary": 45000
    },
    {
      "firstName": "Laura",
      "lastName": "Burnett",
      "salary": 80000
    }
  ]
}

"""
import sqlite3

PATH = os.path.dirname(os.path.abspath(__file__))


def create_db(db_name="test"):
    if os.path.exists(f"{PATH}/{db_name}.db"):
        os.remove(f"{PATH}/{db_name}.db")
    con = sqlite3.connect(f"{PATH}/{db_name}.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE user ("
                "userid INTEGER PRIMARY KEY AUTOINCREMENT, "
                "firstName TEXT, "
                "lastName TEXT, "
                "salary INTEGER, "
                "del INT DEFAULT 0, "
                "UNIQUE(firstName, lastName)"
                ")")
    res = cur.execute("SELECT name FROM sqlite_master")
    print(res.fetchone())
    data = [
        ("Lewis", "Burson", 40700),
        ("a", "aa", 11),
        ("b", "bb", 22),
        ("c", "cc", 33),
        ("d", "dd", 44),
        ("e", "ee", 55),
        ("f", "ff", 66),
    ]
    cur.executemany("INSERT INTO `user` (firstName, lastName, salary) VALUES (?, ?, ?)", data)
    con.commit()
    result = cur.execute("select * from user")
    print(result.fetchall())


class DB:

    def __init__(self, db_name='test'):
        self.db_path = f"{PATH}/{db_name}.db"

    def __enter__(self):
        self.con = sqlite3.connect(self.db_path)

        # self.con.row_factory = sqlite3.Row

        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d

        self.con.row_factory = dict_factory
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()


if __name__ == '__main__':
    create_db()
    # exit()
    with DB() as db:
        cursor = db.cursor()
        sql = f"SELECT count(*) as cnt  FROM `user` where del=0;"
        cursor.execute(sql)
        res = cursor.fetchone()
    print(res)
    with DB() as db:
        cursor = db.cursor()
        sql = f"SELECT * FROM `user` where del=0;"
        cursor.execute(sql)
        res = cursor.fetchall()
    print(res)




