# Log Analysis Project
-----------------------

# Project Overview

This project sets up a PostgreSQL database for a news website.
The provided Python script main.py uses the psycopg2 library to query the database and produce a report that answers the following questions

The reporting tool needed to answer the following questions:

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

# How to Run the Code

- Clone or download the project;
- Make sure you have newsdata.zip the database of website,
<a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">Click Here to Download</a>
- before start, you must creat news database "news" with this command: "psql -d news -f newsdata.sql"
- Run the script with this command: "python main.py"
- You will get results on your terminal;
