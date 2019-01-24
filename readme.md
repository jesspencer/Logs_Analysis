Logs_Analysis

Questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

Requirements: 

1. Python 2.7.15 
2. psycopg2
3. psycopg2.extras
4. Postgresql 9.6

How to run: 

1. Load the data into the database:

psql -d news -f newsdata.sql

2. Connect to the database:

psql -d news

3. Create views:

Create View top_three_articles as 
Select a.slug, a.author, count(a.slug) as views 
From articles a, log l 
Where a.slug = substring(l.path,10) and l.status = '200 OK' 
Group By a.slug, a.author 
Order by views 
desc limit 3; 

Create View top_three_authors as 
Select authors.name, top_three_articles.views 
From authors 
Join top_three_articles 
On top_three_articles.author = authors.id 
Group By authors.name, top_three_articles.views 
Order By top_three_articles.views
desc limit 3;

Create View requests as 
Select date(time) as date, count(*) as http_requests 
From log 
group by date;

Create View errors as 
Select date(time) as date, count(*) as http_404 
From log 
Where status = '404 NOT FOUND' 
group by date;

4. Run python script:

python2.7 Logs_Analysis.py 


