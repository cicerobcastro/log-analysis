#!/usr/bin/python3

import psycopg2


def connect_to_database():
    """Connects to the news database and return a database cursor."""
    try:
        database = psycopg2.connect("dbname=news")
        cursor = database.cursor()
    except:
        print("Failed to connect to the PostgreSQL database.")
        return None
    else:
        return cursor

q1 = 'Question 1: What are the most popular articles of all time?'

query_1 = """SELECT title,
count(*) as list FROM articles JOIN log
ON articles.slug = substring(log.path, 10)
GROUP BY title ORDER BY list DESC LIMIT 3;"""

q2 = 'Question 2: Who are the most popular article authors of all time?'

query_2 = """SELECT authors.name,
count(*) as views FROM articles JOIN authors
ON articles.author = authors.id JOIN log
ON articles.slug = substring(log.path, 10)
WHERE log.status LIKE '200 OK'
GROUP BY authors.name ORDER BY views DESC;"""

q3 = 'On which days did more than 1% of requests lead to errors?'

query_3 = """SELECT * from (SELECT DATE(TIME),round(100.0*sum(case log.status
when '200 OK'  then 0 else 1 end)/count(log.status),3) AS error FROM log group
by DATE(TIME) ORDER BY error DESC) AS subq WHERE error > 1;"""


def queryResult(query):
    database = psycopg2.connect("dbname=news")
    c = database.cursor()
    c.execute(query)
    results = c.fetchall()
    database.close()
    return results


# Consult DB and will print 1 result
def printQuery1(query_1):
    result1 = queryResult(query_1)
    print(q1)
    for result in result1:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


# Consult DB and will print 2 result
def printQuery2(query_2):
    result2 = queryResult(query_2)
    print(q2)
    for result in result2:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


# Consult DB and will print 3 result
def printQuery3(query_3):
    result3 = queryResult(query_3)
    print(q3)
    for result in result3:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')

# Printing results
print("Querying Database...")
printQuery1(query_1)
printQuery2(query_2)
printQuery3(query_3)
