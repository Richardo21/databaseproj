import os
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
# from python_mysql_dbconfig import read_db_config
# from mysql.connector import MySQLConnection
import mysql.connector
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from app.forms import LoginForm, RegistrationForm, Search, Report
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, Item, Account,Branch, Located_At
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import stripe


pub_key = 'pk_test_x1cWwaBJax7f8O4hzycudfYD00xn90rArh'
secret_key = 'sk_test_YnrGPHZyQr9VSKeKclQLMrAw00Gbfjnh6Q'

stripe.api_key = secret_key
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/report', methods = ['POST','GET'])
@login_required
def report():

    report = Report()
    return render_template('report.html',report = report)

@app.route('/portmore-num-sales', methods=['POST','GET'])
def portmoreNumSales():
    listing = []
    if (request.method == "POST"):
        try:
            mySQL_conn = mysql.connector.connect(host='localhost', database='compustore', user='root',
            password='English12_')
            cursor = mySQL_conn.cursor()
            cursor.callproc('num_of_sales')

            for result in cursor.stored_results():
                listing= [result.fetchall()]
                
        
        except mysql.connector.Error as error:
            return ("Failed to execute stored procedure: {}".format(error))

        finally:
            if (mySQL_conn.is_connected()):
                cursor.close()
                mySQL_conn.close()
                return render_template('portmore_num_sales.html',listing = listing)

@app.route('/kingston-num-sales', methods=['POST','GET'])
def kingstonNumSales():
    listing = []
    if (request.method == "POST"):
        try:
            mySQL_conn = mysql.connector.connect(host='localhost', database='compustore1', user='root',
            password='English12_')
            cursor = mySQL_conn.cursor()
            cursor.callproc('num_of_sales')

            for result in cursor.stored_results():
                listing= [result.fetchall()]
                
        
        except mysql.connector.Error as error:
            return ("Failed to execute stored procedure: {}".format(error))

        finally:
            if (mySQL_conn.is_connected()):
                cursor.close()
                mySQL_conn.close()
                return render_template('kingston_num_sales.html',listing = listing)

@app.route('/halfwaytree-num-sales', methods=['POST','GET'])
def halfwaytreeNumSales():
    listing = []
    if (request.method == "POST"):
        try:
            mySQL_conn = mysql.connector.connect(host='localhost', database='compustore2', user='root',
            password='English12_')
            cursor = mySQL_conn.cursor()
            cursor.callproc('num_of_sales')

            for result in cursor.stored_results():
                listing= [result.fetchall()]
                
        
        except mysql.connector.Error as error:
            return ("Failed to execute stored procedure: {}".format(error))

        finally:
            if (mySQL_conn.is_connected()):
                cursor.close()
                mySQL_conn.close()
                return render_template('halfwaytree_num_sales.html',listing = listing)


@app.route('/portmore-branch-top-sales', methods= ['POST', 'GET'])
def portmoreTopSales():
    laptops = []
    if (request.method == "POST"):
        try:
            mySQL_conn = mysql.connector.connect(host='localhost', database='compustore', user='root',
            password='English12_')
            cursor = mySQL_conn.cursor()
            cursor.callproc('top_sales')

            for result in cursor.stored_results():
                laptops= [result.fetchall()]
                
        
        except mysql.connector.Error as error:
            return ("Failed to execute stored procedure: {}".format(error))

        finally:
            if (mySQL_conn.is_connected()):
                cursor.close()
                mySQL_conn.close()
                return render_template('portmore_sales.html',laptops = laptops)


@app.route('/kingston-branch-top-sales', methods= ['POST', 'GET'])
def kingstonTopSales():
    laptops = []
    if (request.method == "POST"):
        try:
            mySQL_conn = mysql.connector.connect(host='localhost', database='compustore1', user='root',
            password='English12_')
            cursor = mySQL_conn.cursor()
            cursor.callproc('top_sales')

            for result in cursor.stored_results():
                laptops= [result.fetchall()]
                
        
        except mysql.connector.Error as error:
            return ("Failed to execute stored procedure: {}".format(error))

        finally:
            if (mySQL_conn.is_connected()):
                cursor.close()
                mySQL_conn.close()
                return render_template('kingston_sales.html',laptops = laptops)

@app.route('/halfwaytree-branch-top-sales', methods= ['POST', 'GET'])
def halfwaytreeTopSales():
    laptops = []
    if (request.method == "POST"):
        try:
            mySQL_conn = mysql.connector.connect(host='localhost', database='compustore2', user='root',
            password='English12_')
            cursor = mySQL_conn.cursor()
            cursor.callproc('top_sales')

            for result in cursor.stored_results():
                laptops= [result.fetchall()]
                
        
        except mysql.connector.Error as error:
            return ("Failed to execute stored procedure: {}".format(error))

        finally:
            if (mySQL_conn.is_connected()):
                cursor.close()
                mySQL_conn.close()
                return render_template('halfwaytree_sales.html',laptops = laptops)

@app.route('/item-search', methods = ['POST','GET'])
def item_search():
    search_items = []
    items = db.session.query(Item).all()
    branch = db.session.query(Branch).all()
    located_at = db.session.query(Located_At).all()
    searchForm = Search()
    searchTerm = request.form['searchTerm']
    # try:
    #     mySQL_conn = mysql.connector.connect(host='localhost', database='compustore', user='root',
    #     password='English12_')
    #     cursor = mySQL_conn.cursor()
    #     cursor.callproc('search',[request.form['searchTerm'],])

    #     for result in cursor.stored_results():
    #         # search_items = result.fetchall()
    #         return(result.fetchall())
    
    # except mysql.connector.Error as error:
    #     return ("Failed to execute stored procedure: {}".format(error))

    # finally:
    #     if (mySQL_conn.is_connected()):
    #         cursor.close()
    #         mySQL_conn.close()
    #      
            # return render_template('search-results.html', search_items= search_items, items = items,
            # searchTerm = searchTerm, located_at=located_at, branch=branch,pub_key = pub_key)

    return render_template('search-results.html', items = items,searchTerm = searchTerm, located_at=located_at, branch=branch, search_items= search_items,pub_key = pub_key)

@app.route('/receipt')
def receipt():
    return render_template('receipt.html')

@app.route('/purchase-item/', methods = ['POST','GET'])
@login_required
def purchase_item():
    #doing a trigger here
    # if (request.method == "POST"):

    #This route should add the items purchased into the Buy DB table

    #     accountIds = db.session.query(Account).all()
    #     for (aid in accountIds):
    #         if (uid == aid):
                
    return redirect(url_for('receipt'))

@app.route('/register', methods = ["GET", "POST"])
def register():
    registerForm = RegistrationForm()
    if ((request.method == 'POST') and (registerForm.validate_on_submit())):
        uname = request.form['uname']
        pword = request.form['pword']
        crdcardno = request.form['crdcardno']
      
        if uname is not None:
            newUser = User(uname, pword)
            db.session.add(newUser)
            newAccount = Account(newUser.uid,crdcardno)
            db.session.add(newAccount)
            db.session.commit()

            flash('Your account has been created successfully!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Fill out all fields.','danger')

    return render_template('register.html', registerForm = registerForm)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('item'))
    loginForm = LoginForm()
    if ((request.method == "POST") and (loginForm.validate_on_submit())):
        # change this to actually validate the entire form submission
        # and not just one field
        if loginForm.uname.data:
            # Get the username and password values from the form.
            uname = request.form['uname']
            pword = request.form['pword']
            # using your model, query database for a user based on the username
            # and password submitted. Remember you need to compare the password hash.
            # You will need to import the appropriate function to do so.
            # Then store the result of that query to a `user` variable so it can be
            # passed to the login_user() method below.
            
            user = User.query.filter_by(uname = uname).first()
           

            if user is not None :
                # get user id, load into session
                login_user(user)

                # remember to flash a message to the user
                flash('You have successfully logged in!','success')
                return redirect(url_for('item'))  # they should be redirected to a secure-page route instead
            else:
                flash('User not found.','danger')
    return render_template("login.html", loginForm= loginForm)


@app.route("/item")
@login_required
def item():
    items = db.session.query(Item).all()
    searchForm = Search()

    return render_template("item.html", items = items, pub_key= pub_key, searchForm = searchForm )

@app.route("/logout")
def logout():
    logout_user()
    flash('You are now logged out.','danger')
    return redirect(url_for('home'))


# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")