import sqlite3
from post import Post


class DatabaseHandler:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cursor = self.connection.cursor()

    def add_post(self, post):
        sql_command = f"""
        INSERT INTO post (title, author, datetime, body)
        VALUES ("{post.title}", "{post.author}", "{post.date}", "{post.body}");
        """
        self.cursor.execute(sql_command)
        self.connection.commit()
        self.connection.close()

    def get_posts(self):
        sql_command = "SELECT * FROM post ORDER BY datetime(datetime) DESC;"
        self.cursor.execute(sql_command)
        results = self.cursor.fetchall()
        self.connection.close()

        posts = []
        for r in results:
            posts.append(Post(r[0], r[1], r[2], r[3]))
        return posts
