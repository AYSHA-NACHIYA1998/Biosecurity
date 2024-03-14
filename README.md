# Biosecurity

**README File**

This README file provides a brief overview of the horticulture pest and disease biosecurity guide web application developed for the COMP639 Studio Project - Semester 1, 2024.

### System Description:
The horticulture pest and disease biosecurity guide web application is designed to provide information on horticulture pests and diseases present in New Zealand, as well as those not currently found in the country. It includes features such as user authentication, role-based access control, profile management, and a comprehensive guide containing detailed information about pests and diseases.

### Login Information for Different Types of Users:
- **Horticulturalists:**
  - Username: aysha@admin.com
  - Password: 12345678

- **Staff:**
  - Username: aysha@staff.com
  - Password: 12345678

- **Administrator:**
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

