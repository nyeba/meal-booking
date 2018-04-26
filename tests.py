import unittest
import requests
import json
import login


class testlogin(unittest.Testcase):

	def test_login(self):
		response = requests.post('/login', name=' nyebaoscar' password ='123456')
		if response.ok:
			return "success"
		else:
		return 	" failed"


class testsignup(unittest.TestCase):


	def testsignup(self):
		signup = request.form['signup']
		response = requests.post('/signup  name ='Antony' password ='123456' repeat ='123456'')
		return  response + "You have successfully signed up"
		else:
		return 	"The  signup test failed"

if __name__ ='__main__':
	unittest.main()