#Creates a guestbook db and inserts a dummy post

import sqlite3
from datetime import datetime

#Extra arguments allow datetime object to be written and read with 'timestamp' data type (not really a type, TEXT affinity)
connection = sqlite3.connect('guestbook.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES);

db = connection.cursor();

sqlite_command = """
CREATE TABLE post (
title TEXT,
author TEXT,
datetime timestamp,
body TEXT); """

db.execute(sqlite_command);

now = datetime.now()

sqlite_command = """
INSERT INTO post (title, author, datetime, body)
VALUES ("Blowin' in the wind", "Bob Dylan", "{0}", "Lorem ipsum dolor sit amet, est ex laudem similique interpretaris, aeque albucius euripidis has ad, id lorem accusamus reformidans ius. Mundi alienum conceptam te nam, quodsi invidunt per ex. At est debet qualisque mnesarchum, mei ne harum sententiae. Est discere sententiae inciderint no, sea ne saepe perpetua, illum elitr usu ne. Viris oblique consulatu est te, ei mei modo dissentiunt efficiantur. Vero illud adipiscing vel te, putant invidunt mea ne.");""".format(now)

db.execute(sqlite_command)
connection.commit()
connection.close()
