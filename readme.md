# Logs_Analysis
## Project Description
This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

Questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

Requirements: 

1. Python 2.7.15 
2. psycopg2
3. Postgresql 9.6


How to run: 

1. Create a Database named "news": 

launch the psql console: psql

create an empty news database: CREATE DATABASE news;

exit psql console: \q

2. Get newsdata.sql file with the database schema and data: 

[newsdata.sql file can be downloaded with this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 

3. Load the data into the database:

psql -d news -f newsdata.sql

4. Connect to the database:

psql -d news

5. Create views:

'''sql Create View top_three_articles as 
Select a.slug, a.author, count(a.slug) as views 
From articles a, log l 
Where a.slug = substring(l.path,10) and l.status = '200 OK' 
Group By a.slug, a.author 
Order by views 
desc limit 3; 
'''

'''sql Create View top_three_authors as 
Select authors.name, top_three_articles.views 
From authors 
Join top_three_articles 
On top_three_articles.author = authors.id 
Group By authors.name, top_three_articles.views 
Order By top_three_articles.views
desc limit 3;
'''

'''sql Create View requests as 
Select date(time) as date, count(*) as http_requests 
From log 
group by date;
'''

'''sql Create View errors as 
Select date(time) as date, count(*) as http_404 
From log 
Where status = '404 NOT FOUND' 
group by date;
'''

'''sql Create View error_percentage as 
Select q1.date as date,
round(q1.errors::numeric,2) as error_percent 
From (select r.date as date,
e.http_404::numeric/r.http_requests*100 as errors
From requests r join errors e on r.date = e.date
Group By r.date, e.http_404, r.http_requests) as q1;
'''

6. Run python script:

python2 la.py

7. Text file la.py_results.txt shows the output that you should get from running the la.py file.  
