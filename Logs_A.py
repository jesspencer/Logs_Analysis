#!/usr/bin /env python2.7

import psycopg2
import psycopg2.extras

text_file = open("results_file.txt", "w")
text_file.truncate()

'#connecting to database'


def connect(database_name="news"):
	'''
	try:
		dict_cur = psycopg2.connect("dbname{}".format(database_name))
		conn = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
		return psycopg2, conn
	
	except psycop2.Error: 
		print "unable to connect to database"
		exit(1)
	'''	
def get_query_results(query):
	dict_cur, conn = connect()
	dict_cur.execute(query)
	results = dict_cur.fetchall()
	text_file.write(results)

def print_top_three_articles(results): 
	text_file.write('Top three articles of all time: \n')
	for row in results: 
		text.write(row[0])
		
def print_top_three_authors(results):
	text_file.write('Top three authors of all time: \n')
	for row in results: 
		text.write(row[0])

def print_top_log_errors(results):
	text_file.write('Days where more than 1% of requests led to errors: \n')
	for row in results:
		text.write(row[0])
		
if __name__== '__main__':
	db, c = connect()
	results = get_query_results("select top_three_articles.slug from top_three_articles;")
	
	dict_cur, conn = connect()
	results = get_query_results("select top_three_authors.name from top_three_authors;")
	
	dict_cur, conn = connect()
	results = get_query_results("select r.date from requests r join errors e on r.date = e.date where e.http_404::numeric/r.http_requests * 100 > 1 group by r.date, e.http_404, r.http_requests;")
	print "results_file.txt has been created" 

dict_cur.close()
text_file.close()	


