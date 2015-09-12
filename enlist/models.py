from django.db import models

class EmailConfirmation(models.Model):
    account = models.OneToOneField(User, null=False, blank=False, related_name="email_confirmation")
    emnail = models.EmailField(null=False, blank=False)
    verified = models.BooleanField(null=False, blank=True, default=False)

    def __str__(self):
        return "%s: %s" % (self.account, ("email verified" if self.verified else "email not verified"))
