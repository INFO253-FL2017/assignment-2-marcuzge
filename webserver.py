"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template, request
import requests
import os

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def index_page():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/about')
def about_page():
	return render_template("about_us.html")

@app.route('/contact', methods=['GET'])
def contact_page():
	return render_template("contact_us.html", notifications=[])

@app.route("/contact", methods=["POST"])
def send_email():
	name = request.form.get("username")
	subject = request.form.get("sub")
	message = "Name: " + name + "\n" + "Subject: " + subject + "\n" + "Message: " +request.form.get("msg")
	notifications = []

	data = {
	    "from": os.environ["INFO253_MAILGUN_FROM_EMAIL"],
        "to": os.environ["INFO253_MAILGUN_TO_EMAIL"],
	    "subject": subject,
	    "text": message,
	}

	auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

	r = requests.post(
		"https://api.mailgun.net/v3/{}/messages".format(os.environ["INFO253_MAILGUN_DOMAIN"]), 
		auth=auth, 
		data=data
		)

	if r.status_code == requests.codes.ok:
		notifications.append("Hi " + name +", your message has been sent")
	else:
		notifications.append("You message was not sent. Please try again later.")

	return render_template("contact_us.html", notifications=notifications)


@app.route('/blog/8-experiments-in-motivation')
def blog1_page():
	return render_template("8-experiments-in-motivation.html")

@app.route('/blog/a-mindful-shift-of-focus')
def blog2_page():
	return render_template("a-mindful-shift-of-focus.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def blog3_page():
	return render_template("how-to-develop-an-awesome-sense-of-direction.html")

@app.route('/blog/training-to-be-a-good-writer')
def blog4_page():
	return render_template("training-to-be-a-good-writer.html")

@app.route('/blog/what-productivity-systems-wont-solve')
def blog5_page():
	return render_template("what-productivity-systems-wont-solve.html")