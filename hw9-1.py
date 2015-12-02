import psutil
from wsgiref.simple_server import make_server

i1= psutil.disk_usage('/')


def hello_world_app(environ, start_response):
	message=""
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	message += "<h1>Disk Info</h1>"
	message += '<div><div id="586417348255479931" align="left" style="width: 100%; overflow-y: hidden;" class="wcustomhtml">'
	message += ("<table width='40%' border=0><tr bgcolor='#DDA0DD'><td>TOTAL DISK </td><td>"+str(i1.total)+"</td>")
	message += ("</tr><tr bgcolor='#DDA0DD'><td>DISK USED</td><td>"+str(i1.used)+"</td>")
	message += ("<tr><td>DISK FREE</td></tr><td>"+str(i1.free)+"</td>")
	message += ("<tr bgcolor='#DDA0DD'><td>USED DISK PERCENTAGE</td><td>"+str(i1.percent)+"</td></table></div>")
	return[bytes(message,'utf-8')]

httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")


httpd.serve_forever()
