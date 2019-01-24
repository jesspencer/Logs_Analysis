#!/usr/bin/en python2.7

'#importing standard library for postgres'
import psycopg2
import psycopg2.extras

'#connecting to database'
conn = psycopg2.connect("dbname=news")

dict_cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

'#Created top_three_articles view, then ran query for the top_three_articles view. see commands to create views in readme.md'
dict_cur.execute( "select top_three_articles.slug from top_three_articles;")
top_three_articles = dict_cur.fetchall()

'#Created top_three_authors view, then ran query for the top_three_authors view. see commands to create views in readme.md'
dict_cur.execute("select top_three_authors.name from top_three_authors;")
top_three_authors = dict_cur.fetchall()

'#Created requests view and errors view, and then ran query for the top_log_errors. see commands to create views in readme.md'
dict_cur.execute("select r.date from requests r join errors e on r.date = e.date where e.http_404::numeric/r.http_requests * 100 > 1 group by r.date, e.http_404, r.http_requests;")
top_log_errors = dict_cur.fetchall()

'#printing results to txt file'
print "Writing to text file ..." 

'#opening textfile and setting up textfile to write results'
text_file = open("results_file.txt", "w")

print "Erasing results of any previous query..." 
text_file.truncate()

'#heading and input for most popular three articles' 
line1 = """
Most popular three articles of all time:
""" +  "\t*" + "%s"  %(top_three_articles)

line2 = """
Most popular three article authors of all time:
""" + "\t*" "%s" %(top_three_authors)
line3 = """
Days which more than 1% of requests lead to errors:
""" + "\t*" + "%s" %(top_log_errors) 

text_file.write(line1)
text_file.write(line2)
text_file.write(line3)

text_file.close()
print "results_file.txt has been created" 

