from flask, import Flask, request, make_response

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    count = int(request.cookies.get('visit-count', 0)) # Ask for a cookie of the name visit-count from the request, starting at 0 by default
    count += 1 # adds 1 to the cookie each time a user visits
    message = 'You have visited this page ' + str(count) + ' times' # returns a message on how many time you visit the page

    # make a response, set cookie, return
    resp = make_response(message) # make_response creates a HTTP body and you pass the the variable message though it.
    resp.set_cookie('visit-count', str(count))
    return resp

app.run()