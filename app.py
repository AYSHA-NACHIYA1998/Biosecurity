from flask import Flask, render_template, request, session, redirect, url_for, flash
from connect import *
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from flask_hashing import Hashing


local_server = True
app = Flask(__name__)
app.secret_key = 'hetroadmin'

hashing = Hashing(app)


class User(UserMixin):
    def __init__(self, id, firstname, lastname, email, password, uid, phone, hiredate):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.uid = uid
        self.phone = phone
        self.hiredate = hiredate



from flask_login import LoginManager

# Initialize the LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Set the login view for unauthorized users
login_manager.login_view = 'login'

# Define a function to load users
@login_manager.user_loader
def load_user(user_id):
    # Fetch user from the database based on user_id
    cursor.execute("SELECT * FROM User WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    
    if user_data:
        # Create a User object with fetched data
        user = User(
            id=user_data['id'],
            firstname=user_data['firstname'],
            lastname=user_data['lastname'],
            email=user_data['email'],
            password=user_data['password'],
            uid=user_data['uid'],
            phone=user_data['phone'],
            hiredate=user_data['hiredate']
        )
        return user
    else:
        return None

@app.route('/')
def index():
    try:
        # Query the database to fetch all user uids
        cursor.execute("SELECT uid FROM User")
        rows = cursor.fetchall()
        if rows:
            uids = [row[0] for row in rows]  # Extract uids from the fetched rows
        else:
            uids = []  # If no rows fetched, initialize uids as an empty list
    except Exception as e:
        print("Error fetching uids:", e)
        uids = []  # If an error occurs, initialize uids as an empty list

    return render_template('index.html', current_user=current_user, uids=uids)

@app.route('/loginh')
def loginh():
  
    return render_template('loginh.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))
from flask import jsonify
from flask import jsonify

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        cursor.execute("SELECT * FROM User WHERE email = %s", (email,))
        user_data = cursor.fetchone()

        if user_data:
            if hashing.check_value(user_data['password'], password, salt='abcd'):  # Check hashed password with salt
                user = User(
                    id=user_data['id'],
                    firstname=user_data['firstname'],
                    lastname=user_data['lastname'],
                    email=user_data['email'],
                    password=user_data['password'],
                    uid=user_data['uid'],
                    phone=user_data['phone'],
                    hiredate=user_data['hiredate']
                )
                login_user(user)
                flash("Login Success", "primary")
                return redirect(url_for('index'))
            else:
                flash("Invalid credentials", "warning")
                return render_template('login.html')
        else:
            flash("Invalid credentials", "warning")
            return render_template('login.html')

    return render_template('login.html')



@app.route('/login_hetro', methods=['POST'])
def login_hetro():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        cursor.execute("SELECT * FROM Register WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and hashing.check_value(user['password'], password, salt='abcd'):  # Provide the correct salt
            flash('Login successful!', 'success')
            session['email'] = email
            return redirect(url_for('index_hetro'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('loginh'))


from flask import session, jsonify

@app.route('/index_hetro')
def index_hetro():
  
    email = session.get('email')

    if email:
      
        cursor.execute("SELECT * FROM Register WHERE email = %s", (email,))
        registers = cursor.fetchall()
        
        if registers:
          
            uids = [register['uid'] for register in registers]
            return render_template('index.html', registers=registers, uids=uids)
        else:
            flash('No records found for this user.', 'error')
            return redirect(url_for('loginh'))
    else:
        flash('Please login first.', 'error')
        return redirect(url_for('loginh'))


@app.route('/all_pests')
def display_all_pests():
    try:
       
        cursor.execute("SELECT * FROM Horticulturepests")
        pests = cursor.fetchall() 
         
    except Exception as e:
        print("Error fetching pests:", e)
        pests = []  

    return render_template('all_pests.html', current_user=current_user, pests=pests )

@app.route('/all_pests_hetro')
def display_all_pests_hetro():
    email = session.get('email')
    registers = None

    if email:
        cursor.execute("SELECT * FROM Register WHERE email = %s", (email,))
        registers = cursor.fetchall()

    try:
        cursor.execute("SELECT * FROM Horticulturepests")
        pests = cursor.fetchall()
    except Exception as e:
        print("Error fetching pests:", e)
        pests = []

    return render_template('all_pests.html', current_user=current_user, registers=registers, pests=pests)

@app.route('/view_pests')
def display_pest_details():
    pest_id = request.args.get('pest_id')

    try:
        pest_id = int(pest_id)
    except (TypeError, ValueError):
        return "Invalid pest ID"

   
    cursor.execute("SELECT * FROM Horticulturepests WHERE id = %s", (pest_id,))
    pest = cursor.fetchone()

    if pest:
        return render_template('view_pests.html', pest=pest)
    else:
        return "Pest not found"

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

      
        hashed_password = hashing.hash_value(password, salt='abcd')

        cursor.execute("SELECT * FROM User WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Email Already Exist", "warning")
            return render_template('/signup.html')

        try:
            cursor.execute("INSERT INTO User (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
            db_connection.commit()
            flash("Signup Successful! Please Login", "success")
            return render_template('login.html')
        except Exception as e:
            print("Error signing up user:", e)
            flash("An error occurred while signing up. Please try again later.", "error")
            return render_template('signup.html')

    return render_template('signup.html')


@app.route('/register_hetro', methods=['POST', 'GET'])
def register_hetro():
    if request.method == "POST":
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        active = request.form.get('active')
        phonenumber = request.form.get('phonenumber')
        address = request.form.get('address')
        datejoined = request.form.get('datejoined')
        password = request.form.get('password')

        # Converting 'active' to boolean
        active = True if active == '1' else False

        # Hash the password
        hashed_password = hashing.hash_value(password, salt='abcd')

        try:
            cursor.execute("INSERT INTO Register (firstname, lastname, email, active, phonenumber, address, dateofjoind, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (firstname, lastname, email, active, phonenumber, address, datejoined, hashed_password))
            db_connection.commit()  # Commit the transaction
            flash("Your record has been saved successfully", "success")
            return redirect('/loginh')
        except Exception as e:
            print("Error saving user record:", e)
            flash("An error occurred while saving your record. Please try again later.", "error")
            return render_template('signup.html')

    # If method is not POST, render the registration form
    return render_template('signup.html')



@app.route('/hetroistdetail')
@login_required
def hetroistdetail():
    try:
        # Query the database to fetch all registers
        cursor.execute("SELECT * FROM Register")
        query = cursor.fetchall()

        # Fetch all user uids
        cursor.execute("SELECT uid FROM User")
        uids = [row['uid'] for row in cursor.fetchall()]
    except Exception as e:
        print("Error fetching data:", e)
        query = []
        uids = []

    return render_template('hetroistdetail.html', query=query, uids=uids)


@app.route("/delete/<string:rid>", methods=['POST', 'GET'])
@login_required
def delete(rid):
    try:
        cursor.execute("DELETE FROM Register WHERE rid = %s", (rid,))
        db_connection.commit()
        flash("Slot Deleted Successfully", "success")
    except Exception as e:
        print("Error deleting record:", e)
        flash("An error occurred while deleting the record.", "error")

    return redirect('/hetroistdetail')

@app.route('/register', methods=['POST', 'GET'])
@login_required
def register():
    if request.method == "POST":
        # Fetching form data
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        active = request.form.get('active')
        phonenumber = request.form.get('phonenumber')
        address = request.form.get('address')
        datejoined = request.form.get('datejoined')
        password = request.form.get('password')

        # Converting 'active' to boolean
        active = True if active == '1' else False

        # Hash the password with salt 'abcd'
        hashed_password = hashing.hash_value(password, salt='abcd')

        try:
            # Inserting new user data into the database
            cursor.execute("INSERT INTO Register (firstname, lastname, email, active, phonenumber, address, dateofjoind, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (firstname, lastname, email, active, phonenumber, address, datejoined, hashed_password))
            db_connection.commit()  # Commit the transaction
            flash("Your record has been saved successfully", "success")
            return redirect('/hetroistdetail')
        except Exception as e:
            print("Error saving user record:", e)
            flash("An error occurred while saving your record. Please try again later.", "error")
            return render_template('hetroist.html')

    # If method is not POST, render the registration form
    return render_template('hetroist.html')

@app.route('/edit/<int:rid>', methods=['POST', 'GET'])
def edit(rid):
    if request.method == "POST":
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        active = request.form.get('active')
        phonenumber = request.form.get('phonenumber')
        address = request.form.get('address')
        datejoined = request.form.get('datejoined')

        active = True if active == '1' else False

        try:
            cursor.execute("UPDATE Register SET firstname=%s, lastname=%s, email=%s, active=%s, phonenumber=%s, address=%s, dateofjoind=%s WHERE rid=%s",
                           (firstname, lastname, email, active, phonenumber, address, datejoined, rid))
            db_connection.commit()
            flash("Details updated successfully", "success")
            return redirect('/hetroistdetail')
        except Exception as e:
            print("Error updating user details:", e)
            flash("An error occurred while updating details. Please try again later.", "error")
            return redirect('/hetroistdetail')

    # If method is not POST, render the edit form with the existing data
    try:
        cursor.execute("SELECT * FROM Register WHERE rid = %s", (rid,))
        posts = cursor.fetchone()
        return render_template('/edit.html', posts=posts)
    except Exception as e:
        print("Error fetching user details:", e)
        flash("An error occurred while fetching user details. Please try again later.", "error")
        return redirect('/hetroistdetail')


@app.route('/staffdetails')
@login_required
def staff_details():
    try:
        cursor.execute("SELECT * FROM User")
        users = cursor.fetchall()
        return render_template('staff.html', users=users)
    except Exception as e:
        print("Error fetching user details:", e)
        flash("An error occurred while fetching user details. Please try again later.", "error")
        return redirect(url_for('index'))

@app.route('/addstaff', methods=['GET', 'POST'])
@login_required
def add_staff():
    if request.method == 'POST':
        # Fetch form data
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        hiredate = request.form.get('hiredate')

        # Hash the password with salt 'abcd'
        hashed_password = hashing.hash_value(password, salt='abcd')

        # Insert new staff member into the database
        try:
            cursor.execute("INSERT INTO User (firstname, lastname, email, password, phone, hiredate) VALUES (%s, %s, %s, %s, %s, %s)",
                           (firstname, lastname, email, hashed_password, phone, hiredate))
            db_connection.commit()  # Commit the transaction
            flash("Staff added successfully!", "success")
            return redirect('/staffdetails')
        except Exception as e:
            print("Error adding new staff member:", e)
            flash("An error occurred while adding the staff member. Please try again later.", "error")

    return render_template('addstaff.html')


@app.route('/edit_profile/<int:id>', methods=['POST', 'GET'])
@login_required
def edit_profile(id):
    if request.method == "POST":
        # Fetch form data
        firstname = request.form.get('firstname')
        email = request.form.get('email')
        password = request.form.get('password')
        uid = request.form.get('uid')

        # Hash the password
        hashed_password = hashing.hash_value(password, salt='abcd')

        try:
            cursor.execute("UPDATE User SET firstname = %s, email = %s, password = %s, uid = %s WHERE id = %s",
                           (firstname, email, hashed_password, uid, id))
            db_connection.commit()
            flash("Profile Updated", "success")
            return redirect('/')
        except Exception as e:
            print("Error updating user profile:", e)
            flash("An error occurred while updating the profile. Please try again later.", "error")

    # Fetch the user's profile details
    try:
        cursor.execute("SELECT * FROM User WHERE id = %s", (id,))
        user_data = cursor.fetchone()
    except Exception as e:
        print("Error fetching user profile:", e)
        user_data = None

    return render_template('/edit_profile.html', user_entry=user_data)

@app.route('/pests')
def show_pests():
    try:
        # Assuming 'cursor' is the MySQL cursor object
        cursor.execute("SELECT * FROM Horticulturepests")
        pests = cursor.fetchall()  # Fetch all rows
    except Exception as e:
        print("Error fetching pests:", e)
        pests = []  # If an error occurs, return an empty list

    return render_template('pests.html', pests=pests)


@app.route('/addpests', methods=['GET', 'POST'])
def add_pest():
    if request.method == 'POST':
        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        presence_in_nz = True if request.form.get('presence_in_nz') == 'on' else False
        primary_image_url = request.form['primary_image_url']
        key_characteristics = request.form['key_characteristics']
        biology_description = request.form['biology_description']
        impacts = request.form['impacts']

        try:
            # Execute an SQL INSERT query to add a new pest
            cursor.execute("INSERT INTO Horticulturepests (CommonName, ScientificName, PresenceInNZ, PrimaryImageURL, KeyCharacteristics, BiologyDescription, Impacts) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (common_name, scientific_name, presence_in_nz, primary_image_url, key_characteristics, biology_description, impacts))
            db_connection.commit()  # Commit the transaction

            flash('New pest added successfully!', 'success')
            return redirect(url_for('show_pests'))
        except Exception as e:
            print("Error adding new pest:", e)
            flash('An error occurred while adding the new pest. Please try again later.', 'error')
            return render_template('addpests.html')

    return render_template('addpests.html')

@app.route('/edit_pest/<int:pest_id>', methods=['GET', 'POST'])
def edit_pest(pest_id):
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Horticulturepests WHERE id = %s", (pest_id,))
    pest = cursor.fetchone()

    if request.method == 'POST':
        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        presence_in_nz = True if request.form.get('presence_in_nz') == 'on' else False
        primary_image_url = request.form['primary_image_url']
        key_characteristics = request.form['key_characteristics']
        biology_description = request.form['biology_description']
        impacts = request.form['impacts']

        try:
            # Execute an SQL UPDATE query to update the pest information
            cursor.execute("UPDATE Horticulturepests SET CommonName = %s, ScientificName = %s, PresenceInNZ = %s, PrimaryImageURL = %s, KeyCharacteristics = %s, BiologyDescription = %s, Impacts = %s WHERE id = %s",
                           (common_name, scientific_name, presence_in_nz, primary_image_url, key_characteristics, biology_description, impacts, pest_id))
            db_connection.commit()  # Commit the transaction

            flash('Pest updated successfully!', 'success')
            return redirect(url_for('show_pests'))
        except Exception as e:
            print("Error updating pest:", e)
            flash('An error occurred while updating the pest. Please try again later.', 'error')
            return render_template('edit_pests.html', pest=pest)

    return render_template('edit_pests.html', pest=pest)


@app.route('/delete_pest/<int:pest_id>', methods=['POST', 'GET'])
def delete_pest(pest_id):
    cursor = db_connection.cursor()

    try:
        # Execute an SQL DELETE query to delete the pest with the given ID
        cursor.execute("DELETE FROM Horticulturepests WHERE id = %s", (pest_id,))
        db_connection.commit()  # Commit the transaction

        flash('Pest deleted successfully!', 'success')
    except Exception as e:
        print("Error deleting pest:", e)
        flash('An error occurred while deleting the pest. Please try again later.', 'error')
    
    return redirect(url_for('show_pests'))

from flask import render_template

@app.route('/triggers')
@login_required
def triggers():
    try:
        # Assuming 'cursor' is the MySQL cursor object
        cursor.execute("SELECT * FROM Trig")
        triggers = cursor.fetchall()  # Fetch all triggers
    except Exception as e:
        print("Error fetching triggers:", e)
        triggers = []  # If an error occurs, return an empty list

    return render_template('triggers.html', triggers=triggers)



from flask import request, redirect, flash
@app.route('/save_profile/<int:id>', methods=['POST'])
@login_required
def save_profile(id):
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        uid = request.form.get('uid')

        # Hash the password with salt 'abcd'
        hashed_password = hashing.hash_value(password, salt='abcd')

        try:
            # Query the database to update the user profile
            cursor.execute("UPDATE User SET username = %s, email = %s, password = %s, uid = %s WHERE id = %s",
                           (username, email, hashed_password, uid, id))
            db_connection.commit()  # Commit the transaction
            flash("Profile Updated", "success")
        except Exception as e:
            print("Error updating user profile:", e)
            flash("An error occurred while updating the profile. Please try again later.", "error")
            return redirect('/hetroistdetail')  # Redirect to the user details page
        
        return redirect('/hetroistdetail')  

    return redirect('/hetroistdetail') 


app.run(debug=True)    
