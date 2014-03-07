#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
		writeForm(self,"")
		
class Rot13(webapp2.RequestHandler):
	def post(self):
		text = self.request.get("text")
		writeForm(self,rot13(text))

def writeForm(self, rot13_text):
	form="""
	<h2>Enter some text to ROT13:</h2>
	<br>
	<form method="post" action="/rot13">
	<textarea name="text" style="height: 100px; width: 400px;">"""+rot13_text+"""</textarea>
	<br>
	<input type="submit">
	</form>
	"""
	self.response.out.write(form)
			
def rot13(input):
	rstring=''
	for c in input:
		r = alterCharacter(c)
		rstring+=str(chr(r))
	return rstring

def alterCharacter(c):
	r = ord(c)
	if oktorot13(c):
		if lowerCaseRange(c):
			if ord(c) > ord('m'):
				r = subtractRot13(c)
			else:
				r = addRot13(c)
		else:
			if upperCaseRange(c):
				if ord(c) > ord('M'):
					r = subtractRot13(c)
				else:
					r = addRot13(c)
	return r

def subtractRot13(c):
	c = chr(ord(c) - 13)
	return ord(c)

def addRot13(c):
	return ord(c) + 13

def lowerCaseRange(c):
	return (ord(c) in xrange(ord('a'), ord('z')+1))

def upperCaseRange(c):
	return ord(c) in xrange(ord('A'), ord('Z')+1)
	
def oktorot13(c):
	if lowerCaseRange(c):
		return True
	if upperCaseRange(c):
		return True
	return False

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/rot13', Rot13)],
debug=True)

