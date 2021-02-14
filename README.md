# Flask-Heroku-Email-Smtp

    I had come across using flask mail to send emails from a "Contact Me" page. Locally not a hiccup. Everything works, cool, alright! 
Only once deployed on Heroku, sending emails immediately throws an internal server error: smtplib.SMTPAuthenticationError: (534,
Tried allowing third party apps/ less secure access, all the common checkpoints..
Not getting any notifications from gmail, nothing.  While looking into this, it seemed to be a similar story of frustration for quite a few people. 
While I did see many answers, like options for add ons, packages, api's, etc., Many claimed these things did not help either. 
Could be for several reasons, thus creating confusion surrounding this. 
All kinds of rabbit holes one could go down here, but obviously you'd like to avoid making a bunch of changes and dissecting your code at this point.
A very useful piece of info I read was "Heroku has nothing to do with sending or not sending email. The Heroku platform just hosts your web service code, it doesn't care how you send email."
Great! So with Flask-Mail, Gmail and SMTP you should have everything you need in order to send an email from your app.
Gmail is just not giving it access at this point.
For something more high volume I'd guess an add-on would be neccessary. But we're just doing a contact me page.


Here is a simple solution by only changing your gmail settings, getting an app-password from your gmail, 
and then passing that into a config variable on Heroku. 

- Once your app is deployed, go your Google account settings. 
- Security > Signing in to Google > Turn on 2 step verification > App passwords
- Get your 16 digit app password
- In Heroku dashboard for your app > settings > config vars
- Enter your 16 digit app-password in place of your actual gmail password in the config variable value.
- e.g.                   key : value
       'MAIL_DEFAULT_SENDER' = 'your new app password'
       
       And that's that. Keep your actual app-password hidden in a environment variable so nobody can get it.
You should only need it once, but keep a record of it somewhere in case. Also even though google reccommends turning off access
to less secure apps, you most likely have to turn access on for it to work with your app.
Keep in mind the config var is only changed on the Heroku server, locally everything stays the same as it was in your file.   
So, this is what worked for me in my particular case. Figured I'd pass it along to help others out that run into the same issue. 

                  

