import psycopg2


# DB = "newsdata"

# db = psycopg2.connect(database=DB)
if __name__ == '__main__':
	db = psycopg2.connect("dbname=news")

	c = db.cursor()
	print("\n")
	print("\n")
	print("Most popular three articles of all time:")

	#################### QUERY 1 ##########################

	query = "Select title, total_views from articles join test_03 on test_03.filtered_path = concat(' ',articles.slug) limit 3;"
	c.execute(query)
	rows = c.fetchall()
	# db.close()
	for(title, total_views) in rows:
		print("{} - {} views".format(title,total_views))
	print("\n")

	print("Most popular article authors of all time:")

	#################### QUERY 2 ##########################

	query2 = "select author_title_slug.name as name, sum(test_03.total_views) as total_views from author_title_slug, test_03 where test_03.filtered_path = concat(' ',author_title_slug.slug) group by name order by total_views desc limit 3;"
	c.execute(query2)
	rows = c.fetchall()
	# db.close()
	for(name, total_views) in rows:
		print("{} - {} views".format(name,total_views))
	print("\n")

	print("Days did more than 1% of requests lead to errors:")

	#################### QUERY 3 ##########################

	query3 = "select total_requests.date, round((100.0*error_log.error/total_requests.error),2) as percent from error_log,total_requests where error_log.date = total_requests.date order by percent desc limit 1;"
	c.execute(query3)
	rows = c.fetchall()
	db.close()
	for(date , percent) in rows:
		print("{} - {} %".format(date ,percent))
	print("\n")







