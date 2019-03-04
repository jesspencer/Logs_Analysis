# Logs_Analysis
## Project Description
This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions.

## Questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Requirements:

1. Python 2.7.15
2. psycopg2
3. Postgresql 9.6


## How to run:

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

```sql
CREATE VIEW top_three_articles AS
SELECT a.title, a.author, count(a.slug) AS views
FROM articles a, log l
WHERE a.slug = substring(l.path,10)
AND l.status = '200 OK'
GROUP BY a.title, a.author
ORDER BY views DESC
LIMIT 3;
```

```sql
CREATE VIEW article_views AS
SELECT count(log.path) AS views, articles.author AS author_number
FROM log, articles
WHERE substring(log.path, 10) = articles.slug
GROUP BY articles.author
ORDER BY views DESC;
```

```sql
CREATE VIEW top_three_authors AS
SELECT authors.name AS name,
article_views.views AS views
FROM authors JOIN article_views
ON authors.id = article_views.author_number
ORDER BY views DESC
LIMIT 3;
```

```sql
CREATE VIEW requests AS
SELECT date(time) as date, count(*) AS http_requests
FROM log
GROUP BY date;
```

```sql
CREATE VIEW errors AS
SELECT date(time) AS date, count(*) AS http_404
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY date;
```

```sql
CREATE VIEW error_percentage AS
SELECT q1.date AS date,round(q1.errors::numeric,2) AS error_percent
FROM (SELECT r.date AS date,
e.http_404::numeric/r.http_requests*100 AS errors
FROM requests r
JOIN errors e
ON r.date = e.date
GROUP BY r.date, e.http_404, r.http_requests) AS q1;
```

6. Run python script:

python2 la.py

7. Text file la.py_results.txt shows the output that you should get from running the la.py file.  
