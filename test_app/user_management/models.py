from django.db                          import models
from django.utils.translation           import ugettext_lazy as _
from django.contrib.auth.models         import User
from localflavor.generic.models         import IBANField
from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES


class UserInformation(models.Model):
    picture      = models.ImageField(_('Picture'     ), upload_to="%Y/%m/%d"                              )
    last_name    = models.CharField (_('last name'   ), max_length=20                                     )
    first_name   = models.CharField (_('first name'  ), max_length=20                                     )
    IBAN_account = IBANField        (_('IBAN account'), include_countries=IBAN_SEPA_COUNTRIES, unique=True)

    account_manager = models.ForeignKey(verbose_name=_('account manager'), to=User             )

    class Meta:
        verbose_name        = _('User information' )
        verbose_name_plural = _('Users information')

        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return u'{} {}'.format(self.first_name, self.last_name)
