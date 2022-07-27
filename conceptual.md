### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

	* PostgreSQL is an open-source relational database. It uses and extends the SQL querying language.  It safely and reliably stores data.

- What is the difference between SQL and PostgreSQL?

	* SQL is a querying language on its own ("SELECT * FROM pets WHERE...").  PostgreSQL builds upon that (and the SQL standard) with a more efficient and easier language to create data types, build out custom functions, and create and fill tables.

- In `psql`, how do you connect to a database?

	* Typically you would enter the terminal command 'psql DBNAME' to open psql and connect.  If already connected to psql, you would use '\c DBNAME'

- What is the difference between `HAVING` and `WHERE`?

	* HAVING determines which grouped results to keep (if grouped)
	
	* WHERE decides which rows to use (filter which rows get included)

- What is the difference between an `INNER` and `OUTER` join?

	* INNER joins only the rows that match the condition in both tables (this is the default)
	* OUTER joins match all the rows from one table to any matching rows from the second table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

	* LEFT OUTER matches all rows from the first defined table (left) with matching rows from the second table (right)
	
	* RIGHT OUTER does the opposite - the matching rows from the first table (left) are joined with all the rows from the second table (right)

- What is an ORM? What do they do?

	* An ORM (Object Relational Mapping) tool allows for easier querying and manipulation of data from a database using an object-oriented approach (in our case with SQLAlchemy, with NO SQL queries at all)
	* An ORM library is a completely ordinary library that encapsulates the code needed to manipulate the data, so instead of using SQL, you interact directly with an object in the same language you're using.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  
  * Client-side requests (such as with AJAX) can be useful when using AJAX libraries, don't need to use Flask with your API, or are looking to connect to the HTTP faster.
  * Server side requests are needed in cases where a Same-Origin Policy may prevent browser side requests, you need the server to store/process the data, OR you have a required password or key to access the API.

- What is CSRF? What is the purpose of the CSRF token?

	* CSRF stands for Cross-Site Request Forgery and is an attack that forces authenticated users to submit a request to a Web app against which they are currently authenticated.
	* A token blocks this cross-site functionality from occurring by checking that the token of the form is from the legitimate source and not from a bad actor.

- What is the purpose of `form.hidden_tag()`?

	* form.hidden_tag() template argument generates a hidden field that includes a token that is used to prevent against CSRF attacks.  Without this, the form is not protected.  With it, Flask-WTF does all the 'heavy lifting' on token generation.
