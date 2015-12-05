#---------------------------------------------------------------------|
#                             output                                  |
#---------------------------------------------------------------------|
#                     DB NAME IS : z00.sqlite                         |
#---------------------------------------------------------------------|
#abdullahs-MacBook-Pro-2:desktop abdullah$ python3 hw9-2.py           |
#Serving on port 8000...                                              |
#127.0.0.1 - - [05/Dec/2015 16:12:47] "GET / HTTP/1.1" 200 216        |
#count: 333                                                           |
#animal: Test2                                                        |
#Submit: Submit+Query                                                 |
#127.0.0.1 - - [05/Dec/2015 16:13:05] "POST / HTTP/1.1" 200 309       |
#---------------------------------------------------------------------|

import sqlite3
from wsgiref.simple_server import make_server

def get_form_vals(post_str):
	form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
	return form_vals

def hello_world_app(environ, start_response):
	#print("ENVIRON:", environ)
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)

	conn = sqlite3.connect("z00.sqlite")
	cursor = conn.cursor()

	if(environ['REQUEST_METHOD'] == 'POST'):
		message += "<br>Your data has been recorded:"
		request_body_size = int(environ['CONTENT_LENGTH'])
		request_body = environ['wsgi.input'].read(request_body_size)
		form_vals = get_form_vals(request_body)
		cursor.execute("insert into animal_count(name, count) values(?, ?)", (form_vals["animal"], form_vals["count"]))
		for item in form_vals.keys():
			print (item + ": " + form_vals[item])
			message += "<br/>"+item + " = " + form_vals[item]
	
	
	conn.commit()
	conn.close()

	message += "<h1>Welcome to the Zoo</h1>"

	message += "<br><h3>POST MeThoD</h3>"
	message += "<form method='POST'><br>Add Animal:<input type=text name='animal'>"
	message += "<br><br>Add Count:<input type=text name='count'>"
	message += "<br><br><input type='submit' name='Submit' ></form>"



	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")
httpd.serve_forever()

