Guardians Challenge: SQL Injection
Overview
Welcome to the Guardians Challenge! This repository contains a simple web application built with Flask and SQLite, designed to demonstrate an SQL injection vulnerability. Your task is to identify and exploit the vulnerability and then fix it to secure the application.

Challenge Description
Vulnerability
The provided Flask application contains a vulnerability that allows SQL injection. The vulnerability is present in the login functionality, where user inputs are directly embedded into SQL queries without proper sanitization.

Objective
Exploit the Vulnerability:

Test the login endpoint to bypass authentication using SQL injection techniques.
Fix the Vulnerability:

Modify the application to use parameterized queries to prevent SQL injection.
Files
vulnerable_app.py: Contains the code for the vulnerable web application.
fixed_app.py: Contains the code for the fixed web application with SQL injection mitigated.
Getting Started
Prerequisites
Make sure you have Python 3 and Flask installed. If not, you can install Flask using pip:

bash
Copy code
pip install Flask
Running the Vulnerable Application
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/guardians-challenge.git
cd guardians-challenge
Run the vulnerable application:

bash
Copy code
python vulnerable_app.py
The application will be running on http://127.0.0.1:5000. You can use tools like curl, Postman, or a simple script to interact with the /login endpoint.

Exploiting the Vulnerability
To test the vulnerability, send a POST request to the /login endpoint with the following payload:

Username: ' OR '1'='1
Password: anything
Running the Fixed Application
Ensure that the application is not running.

Run the fixed application:

bash
Copy code
python fixed_app.py
The fixed application will also run on http://127.0.0.1:5000. The /login endpoint should now be secure against SQL injection.

Contributing
Feel free to fork the repository, make improvements, and submit a pull request. If you have any questions or issues, open an issue on the GitHub repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
khanabdulmajid548003@gmail.com


