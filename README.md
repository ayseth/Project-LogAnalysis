# Project: Logs Analysis

# Questions
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)



### Requirements
* Linux/VM
* Python 
* psycopg2
* PSQL

## Installation

* To load the data cd into the directory where the project was extracted and use the command 

  ` psql -d news -f newsdata.sql`

* Once you have the data loaded into your database, connect to your database using 

  `psql -d news`

## Views Required:

```
Create view author_title as 
select title, name 
from articles 
join authors on articles.author = authors.id;

Create view total_count as 
select path, count(*) as total 
from log 
group by path 
order by total desc;

Create view test_01 as 
select replace(path, '/article/', ' ') 
from log;

Create view test_02 as 
select replace(replace, '/', ' ') as filtered_path 
from test_01;

Create view test_03 as 
select filtered_path, count(*) as total_views 
from test_02 
group by filtered_path 
order by total views desc;

Create view author_title_slug as 
select articles.slug, articles.title,authors.name 
from authors,articles 
where articles.author = authors.id;

Create view error_log as 
select date(time), count(*) as error 
from log 
where status != '200 OK' group by date(time) 
order by date(time);

Create view total_requests as 
select date(time), count(*) as error 
from log 
group by date(time) 
order by date(time) ;