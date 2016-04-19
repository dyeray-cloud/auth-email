import webapp2
from google.appengine.api import users
from google.appengine.api import mail
import string
import random

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            email_testers = ['<recipient@address>']
            service = "Service1"
            sender = user.email()
            mail.send_mail(
                sender=sender,
                to=email_testers,
                body=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20)),
                subject="prueba")
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.email(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))

        self.response.out.write('<html><body>%s</body></html>' % greeting)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
