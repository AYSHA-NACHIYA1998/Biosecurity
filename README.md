# Biosecurity

**README File**

This README file provides a brief overview of the horticulture pest and disease biosecurity guide web application developed for the COMP639 Studio Project - Semester 1, 2024.

### System Description:
The horticulture pest and disease biosecurity guide web application is designed to provide information on horticulture pests and diseases present in New Zealand, as well as those not currently found in the country. It includes features such as user authentication, role-based access control, profile management, and a comprehensive guide containing detailed information about pests and diseases.

### Login Information for Different Types of Users:
 
- **Administrator:**
  - Username: aysha@admin.com
  - Password: 12345678

- **Staff:**
  - Username: aysha@staff.com
  - Password: 12345678

- **Horticulturalist:**
  - Username: aysha@hetro.com
  - Password: 12345678

### Files Included:
1. **app.py:** Python Flask application file containing the main application logic.
2. **templates:** Directory containing HTML templates for different pages of the web application.
3. **static:** Directory containing static files such as CSS stylesheets, JavaScript files, and images.
4. **requirements.txt:** File listing all required Python packages for the application.
5. **biosecurity.sql:** MySQL script for creating and populating the database.
6. **README.md:** Markdown file providing instructions and information about the project.
7. **.gitignore:** File specifying which files and directories to ignore in version control.

 ## Note  
  We need to reload the server on PythonAnywhere if the error message 'Internal Server Error' appears to correct it.

  
### Project Structure:
- The application logic is implemented in `app.py`, following the Flask framework.
- HTML templates for various pages are stored in the `templates` directory.
- Static files like CSS stylesheets, JavaScript files, and images are stored in the `static` directory.
- The `biosecurity.sql` file contains SQL scripts for creating and populating the database.

### Instructions for Running the Application:
1. Clone the repository from GitHub: [Biosecurity Repository](https://github.com/AYSHA-NACHIYA1998/Biosecurity.git).
2. Install the required Python packages listed in `requirements.txt`.
3. Set up a MySQL database using the provided `biosecurity.sql` script.
4. Modify the database connection settings in `app.py` if necessary.
5. Run the Flask application using the command `python app.py`.
6. Access the application through the provided PythonAnywhere URL: [Biosecurity Web App](http://aysha1157662.pythonanywhere.com/).

 Description of Role-based Login Pages in the Horticulture Pest and Disease 
Biosecurity Guide Web Application 

# 1 Admin/Staff Login Page: 
• This page is intended for users with roles of "Staff" and "Administrator". 
• The page extends from a base template called 'auth.html', suggesting a 
consistent design and layout across multiple pages. 
• The page displays a heading "Admin / Staff Login" with a horticulture-themed 
design. 
• Flash messages, if any, are displayed to notify users of any relevant information 
or errors. 
• A form is presented where users can input their email address and password. 
• Upon submitting the form, the data is sent to the "/login" route using the POST 
method. 
• If users are new and wish to register, they can click on the "Signup" link, which 
directs them to the registration page. 
• Users who identify as "Horticulturalists" can click on the "Login" link provided 
at the bottom of the form to switch to the Horticulturalists' login page.

# 2 Horticulturalists Login Page: 
• This page is specifically designed for users with the role of "Horticulturalists". 
• Similar to the Admin/Staff login page, it extends the 'auth.html' base template 
for consistency. 
• The page features a heading "Horticulturalists Login" with a horticulture
themed design. 
• Flash messages, if any, are displayed similar to the Admin/Staff login page. 
• A form allows users to input their email address and password. 
• Upon form submission, the data is sent to the "/login_hetro" route using the 
POST method. 
• Users who want to register can click on the "Signup" link, redirecting them to 
the registration page. 
• Users who identify as "Admin/Staff" can switch to the Admin/Staff login page 
by clicking on the "Login" link provided at the bottom of the form.

# User Roles and Permissions 
# 1. Horticulturalists: 
• Can view the biosecurity guide. 
• Can manage their own profile (update personal information and change 
password). 
• Have access to view detailed information about horticulture pests and diseases, 
including primary images, common names, scientific names, key 
characteristics, biology/description, impacts, and additional images. 
# 2. Staff: 
• In addition to horticulturalists' privileges, staff members have additional 
permissions: 
• Can manage their own profile (update personal information and change 
password). 
• Can view horticulturalists' profiles. 
• Can manage the biosecurity guide, including adding, updating, and 
deleting details and images, such as selecting the primary image. 
# 3. Administrators: 
• Have full access to the system and all features. 
• In addition to staff and horticulturalists' privileges, administrators have the 
following permissions: 
• Can manage their own profile (update personal information and change 
password). 
• Can manage horticulturalists (view, add, update, and delete). 
• Can manage staff (view, add, update, and delete). 
• Can manage the biosecurity guide, including adding, updating, and 
deleting details and images.. User Roles and Permissions 
