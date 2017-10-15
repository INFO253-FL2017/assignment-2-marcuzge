 1. What is the function of the following technologies in your assignment:
    1. HTML: Marks up language that provides the structure, and static content
    2. CSS: provides styling for HTML files, to make the page looks good
    3. JavaScript: controls submitting form logic, check whether all fields are filled in before submmiting
    4. Python: The server side programming language for Flask framework, configures routes and handles GET, POST requests. 
    5. Flask: an extensible web microframework for building web applications with Python.
    6. HTTP:  Protocol for GET and POST requests to transfer data
    7. GET and POST requests: GET is to get data/html file from the server, whereas POST is to send new data to the server. In the case of this project, submitting the form to send the email is a POST request.

 2. How does HTML, CSS, and JavaScript work together in the browser for this assignment?
    HTML provides the structure of pages with raw content using different html tags, CSS style the HTML elements to make blog pages, contact us and about pages looks good. Javascript provides interactions, notifications and form validation.



 3. How does Python and Flask work together in the server for this assignment?
    Python is the programming language for server side rendering, Flask framework won't work without python. Python configures differents routes in this project. The Flask request module helps us to get data from the form and the request module of python help us with GET and POST requests. In the case of this project, we are using it with mailgun api to send an email using input user provided.


 4. List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request
    "GET /index Status OK 200 - Gets index page
    "GET /about Status OK 200 - Gets about us page
    "GET /contact Status OK 200 - Gets contact us page
    "POST /contact Status OK 200 - Posts request for sending email using external mailgun api
    "GET /blog/a-mindful-shift-of-focus Status OK 200 - Gets blog post
    "GET /blog/8-experiments-in-motivation Status OK 200 - Gets blog post
    "GET /blog/training-to-be-a-good-writer Status OK 200 - Gets blog post
    "GET /blog/what-productivity-systems-wont-solve Status OK 200 - Gets blog post
    "GET /blog/how-to-develop-an-awesome-sense-of-direction Status OK 200 - Gets blog post
    "GET /static/css/style.css Status OK 200 Gets css stylesheet
    "GET /static/js/script.js Status OK 200 Gets javascript file



 
