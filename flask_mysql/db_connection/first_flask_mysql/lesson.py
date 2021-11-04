# send objects to database. Will be different everytime we fill out a form
# user pair statements to inject variables
# variables are distinguished by " %(data dictionary keyname)s "
# fstrings leave us to security issues

query = "INSERT INTO friends (first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s );"
data = {
    "first_name" : "Adrien",
    "last_name" : "Dion",
    "email" : "adion@codingdojo.com"
}

query = "UPDATE friends SET first_name=%(fn)s WHERE id=%(id_num)s; "
data = {
    "fn" : # possibly a value from a form,
    "id_num": # possibly a value from the url,
}
mysql.query_db(query,data)

query = "SELECT * FROM users WHERE email = %(email)s;"
data = { 'email' : request.form['email'] }
result = mysql.query_db(query, data)

# Correct Way:
query = "SELECT * FROM users WHERE email = %(email)s;"
    
# the placeholder variable is called email
# it must match the key name in the data dictionary
data = { 
    # this 'email' Key in data must be named to match the placeholder in the query.
    'email' : request.form['email'] 
}
result = mysql.query_db(query, data)

    



