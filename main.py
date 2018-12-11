import psycopg2

q1 = 'Question 1: What are the most popular articles of all time?'

query_1 = """(SELECT title,
count(*) as views FROM articles JOIN log
ON articles.slug = substring(log.path, 10)
GROUP BY title ORDER BY views DESC LIMIT 3;)"""

q2 = 'Question 2: Who are the most popular article authors of all time?'

query_2 = """(SELECT authors.name, 
count(*) as views FROM articles 
JOIN authors 
ON articles.author = authors.id JOIN log
ON articles.slug = substring(log.path, 10)
WHERE log.status LIKE '200 OK'
GROUP BY authors.name ORDER BY views DESC;)"""

q3 = 'Question 3: On which days more than 1% of the requests led to error?'

query_3 = """(SELECT round((stat*100.0)/visitors, 3) as
result, to_char(errortime, 'Mon DD, YYYY')
FROM errorcount ORDER BY result desc limit 1;)"""

#get informations from db

def queryResult(sql_query):
    db = psycopg2.connect('dbname=news')
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results

result1 = queryResult(query_1)
result2 = queryResult(query_2)
result3 = queryResult(query_3)

#results of querys
def result(reslt):
    for i in range(len(reslt)):
        title = reslt[i][0]
        res = reslt[i][1]
        print("\t" + "%s - %d" % (title, res) + " views")

print(q1)
result(result1)
print(q2)
result(result2)
print(q3)
print("\t" + result3[0][1] + " - " + str(result3[0][0]) + "%")