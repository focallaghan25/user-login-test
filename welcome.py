#!/usr/bin/env python
#
#
# LOGIN SYSTEM
# This is a basic login system that does nothing more
# than register a user to a database and allows that
# user to log in. It verifies the user identity and
# welcomes them on the next page. It is also an exmaple
# of simple hashing and salting of passwords.
#
# WELCOME.PY
# A simpe output file for valdiating a user and creating
# a welcome message.
# 
#
# AUTHOR: Robert Barry
# DATE CREATED: August 5, 2012
# DATE CHANGED: August 5, 2012
# WEB ADDRESS: http://rb-login-rb.appspot.com/signup
#
import webapp2
from users import *
from hashing import *

# Handler for the welcome page
class MainHandler(webapp2.RequestHandler):
    def get(self):
	# Get the cookie data for use in the welcome page
	name = self.request.cookies.get('username')
	user_id = self.request.cookies.get('user-id')

	# Get the user from the database by using the user name from the cookie
	user = db.GqlQuery("SELECT * FROM Users WHERE user_name=:1", name).get()

	# Get the user's unique id
	id = user.key().id()
	
	# Verify that the retreived user id is the same as the hashed
	# user id are one and the same. If so, welcome the user, else
	# return to the signup page.
	if valid_hash(str(id), "", user_id):
	    self.response.out.write("<h1>Welcome, %s!</h1>" % name)
	else:
	    self.redirect("/signup")
 
app = webapp2.WSGIApplication([('/welcome', MainHandler)],
                              debug=True)
