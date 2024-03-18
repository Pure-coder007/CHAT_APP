from flask import Flask, render_template
from wtform_fields import *
from models import * 
from models import db
from mysql.connector import Error
# import mysql.connector



# Configure app
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:language007@localhost/chat'

# db = SQLAlchemy(app)

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    if  reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

       
        
        # Adding user to database
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return f"User {username} added successfully!"
    
    return render_template('index.html', form=reg_form)


if __name__ == '__main__':
    app.run(debug=True)