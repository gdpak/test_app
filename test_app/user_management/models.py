from django.db                          import models
from django.utils.translation           import ugettext_lazy as _
from localflavor.generic.forms          import IBANFormField
from django.contrib.auth.models         import User
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES


class UserInformation(models.Model):
    last_name    = models.CharField(_('last name'   ), max_length=20                        )
    first_name   = models.CharField(_('first name'  ), max_length=20                        )
    IBAN_account = IBANFormField   (_('IBAN account'), include_countries=IBAN_SEPA_COUNTRIES)

    account_manager = models.ForeignKey(User, verbose_name=_('account manager'))

    class Meta:
        verbose_name        = _('User information' )
        verbose_name_plural = _('Users information')

    def __str__(self):
        return u'{} {}'.format(self.first_name, self.last_name)
