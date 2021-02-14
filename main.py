###### SEE THE README FILE FOR OTHER STEPS AND INSTRUCTIONS ###########
###### THESE ARE THE CODE BLOCKS FOR BACKEND SENDING EMAIL SECTION #####

from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail = Mail(app)
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'

########## CONFIGURE YOUR FLASK MAIL SETUP ################

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.environ.get('MAIL_PASSWORD')
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get('MAIL_DEFAULT_SENDER')
mail.init_app(app)

############ THIS IS THE CONTACT-ME FORM ON YOUR WEBSITE ###############

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired()])
    message = StringField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")

############ THIS IS THE APP ROUTE TO YOUR HTML PAGE'S FUNCTIONALITY #######
########### TAKING DATA FROM THE FORM AND EMAILING IT USING FLASK-MAIL, SMTP AND GMAIL

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        msg = Message(email, sender=os.environ.get('MAIL_DEFAULT_SENDER'),
                      recipients=[os.environ.get('MAIL_DEFAULT_SENDER')])
        msg.body = f"{name},\n{email},\n {message}"
        mail.send(msg)
        return redirect(url_for('get_all_posts'))
    return render_template("contact.html", form=form, current_user=current_user)

###### YOU MUST CONFIGURE YOUR GMAIL ACCOUNT TO ACCEPT ACCESS FROM LESS SECURE APPS
###### YOU MUST GET A 16 DIGIT APP-PASSWORD FROM YOUR GMAIL


