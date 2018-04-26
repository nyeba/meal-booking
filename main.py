#signup#




from flask import Flask  
import jsonify
import request 
import make_response 
import jwt
import datetime
from functools import wraps
from flask_restful import Resource, Api


class Login(Resource):

	app.config['SECRET_KEY'] = 'interestingsecretkey'

	def token_required(f):
		@wraps(f)
		def decorated(*args, **wargs):
			token = request.args.get('token')

			if not token:
				return jsonify({'message' :'Token is missing'}), 403

			try:
				data = jwt.decode(token, app.config['SECRET_KEY'])

			except:
				return jsonify({'message' : 'Token is missing or not correct'}), 403
				

			return	f(*args, **wargs)


        from flask import Flask
import data.logdata
from flask_restful import Resource, Api


class SignUp(Form, Resource):
	name=StringField('Name', [validators.length(min=1, max=50)])
	username = StringField('Username', [validators.length(min=4, max=25)])
	email = StringField('Email', [validators.length(min=6, max=50)])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords do not match')
		])

	confirm = PasswordField('Confirm password')



@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method =='POST' and form.validate():
		return 

		return decorated
	

    
    def login( name , password):
    	auth =request.authorization


        if auth.username ='username' and auth.password == 'password':
        	token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, app.config['SECRET_KEY'])

        	return jsonify({'token' : token})


		return  make_response('Could not verify', 401, {'www-Authenticate' : 'Basic realm ="Login Required"})


	api.add_resource(Login, '/auth/login')
