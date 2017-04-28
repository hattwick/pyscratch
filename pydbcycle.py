# iterating database entries and calculatios

import sqlite3
import logging

logging.warning('Starting new session!')

with sqlite3.connect("test.db") as connection:
    c = connection.cursor()

    # Query types
    sql = {'minimum': "SELECT min(population) FROM population",
           'maximum': "SELECT max(population) FROM population",
           'average': "SELECT avg(population) FROM population"}
