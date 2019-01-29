#!/usr/bin/env python2.7

# importing standard library for postgres
import psycopg2
from datetime import datetime

'#database'

DBNAME = "news"

'#querying the database'

query_1 = 'select * from top_three_articles;'

query_2 = 'select * from top_three_authors;'


query_3 = 'select * from error_percentage where error_percent > 1;'

'#answering questions about data'

ques1 = 'Ques 1: What are the most popular three articles of all time?'
ques2 = 'Ques 2: Who are the most popular article authors of all time?'
ques3 = 'Ques 3: On which days did more than 1% of requests lead to errors?'

'#function call to run script'

if __name__ == '__main__':
    conn = psycopg2.connect(database=DBNAME)
    curr = conn.cursor()

    curr.execute(query_1)
    res = curr.fetchall()
    print ques1
    for i in range(len(res)):
        print i+1, ')', res[i][0], '--', res[i][2]
    print''

    curr.execute(query_2)
    res = curr.fetchall()
    print ques2
    for i in range(len(res)):
        print i+1, ')', res[i][0], '--', res[i][1]
    print ''

    curr.execute(query_3)
    res = curr.fetchall()
    print ques3
    for i in range(len(res)):
    	objDate = datetime.strptime(str(res[i][0]), '%Y-%m-%d')
    	longdate = datetime.strftime(objDate, '%b %d, %Y')
        print i+1, ')', longdate,'--', str(res[i][1]) + '%','errors'
    print ''

    conn.close()
