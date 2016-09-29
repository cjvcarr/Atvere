# make_server is used to create this simple python webserver
from wsgiref.simple_server import make_server
import Andris

# Function that is ran when a http request comes in
def light_app(env, start_response):
    
    # set some http headers that are sent to the browser
    status = '200 OK'
    headers = [('Content-type', 'text/html')] 
    start_response(status, headers)

    # What did the user ask for?
    if env["PATH_INFO"] == "/red":
        print("user asked for /red")
        Andris.cleanLed()
        Andris.redOn()
        return "<!DOCTYPE html><html><head><title>\"Lights\"</title></head><body><a title=\"Green\" href=\"/green\">Off</a></body></html>"          

    elif env["PATH_INFO"] == "/green":
        print("user asked for /green")
        Andris.cleanLed()
        Andris.greenOn()
        return "<!DOCTYPE html><html><head><title>\"Lights\"</title></head><body><a title=\"Blue\" href=\"/blue\">On</a></body></html>"          

    elif env["PATH_INFO"] == "/blue":
        print("user asked for /blue")
        Andris.cleanLed()
        Andris.blueOn()
        return "<!DOCTYPE html><html><head><title>\"Lights\"</title></head><body><a title=\"Orange\" href=\"/orange\">On</a></body></html>" 

    elif env["PATH_INFO"] == "/orange":
        print("user asked for /orange")
        Andris.cleanLed()
        Andris.greenOn()
	Andris.redOn()
        return "<!DOCTYPE html><html><head><title>\"Lights\"</title></head><body><a title=\"Aqua\" href=\"/aqua\">On</a></body></html>"

    elif env["PATH_INFO"] == "/aqua":
        print("user asked for /aqua")
        Andris.cleanLed()
        Andris.greenOn()
	Andris.blueOn()
        return "<!DOCTYPE html><html><head><title>\"Lights\"</title></head><body><a title=\"White\" href=\"/white\">On</a></body></html>"

    elif env["PATH_INFO"] == "/white":
        print("user asked for /white")
        Andris.cleanLed()
        Andris.greenOn()
	Andris.redOn()
	Andris.blueOn()
        return "<!DOCTYPE html><html><head><title>\"Lights\"</title></head><body><a title=\"Off\" href=\"/off\">On</a></body></html>"  

    else:
        print("user asked for something else")
	Andris.cleanLed()
        return "<!DOCTYPE html><html><head><title>\"Lights\"</title></head><body><a title=\"Red\" href=\"/red\">On</a></body></html>"          

# Create a small python server
httpd = make_server("", 8001, light_app)
print "Serving on port 8001..."
print "You can open this in the browser http://192.168.1.xxx:8001 where xxx is your rpi ip aadress"
print "Or if you run this server on your own computer then http://localhost:8001" 
httpd.serve_forever()
