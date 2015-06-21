from random                   import choice
from string                   import digits
from string                   import ascii_uppercase
from django.utils.translation import ugettext_lazy as _

from user_management.iban_specification import IBAN_SPCIFICATION_CONFIG

mixed   = ascii_uppercase + digits
letters = ascii_uppercase


class IBANGenerator(object):
    string_randomization_map = {
        'c' : lambda length: u''.join(choice(mixed  ) for _ in range(length)),
        'n' : lambda length: u''.join(choice(digits ) for _ in range(length)),
        'a' : lambda length: u''.join(choice(letters) for _ in range(length)),
    }

    def checksum(self, country_code, bank, account):
        value = bank + account + country_code + '00'
        value = value.upper()
        value_digits = ''
        for x in value:
            if '0' <= x <= '9':
                value_digits += x
            elif 'A' <= x <= 'Z':
                value_digits += str(ord(x) - 55)
            else:
                raise Exception('{} is not a valid character for IBAN.'.format(x))
        return '%02d' % (98 - int(value_digits) % 97)

    def calc_iban(self, country, bank, account):
        account  = account.zfill(country.account_field_length)
        checksum = self.checksum(country.country_code, bank, account)
        return country.country_code + checksum + bank + account

    def randomize_field(self, field_specification):
        return "".join([
            self.string_randomization_map[part.data_type](part.length)
            for part in field_specification])

    def generate(self, country_code=None, bank=None, account=None):
        result = {
            'bank'             : bank,
            'status'           : True,
            'account'          : account,
            'country_code'     : country_code,
            'generator_message': _('Generation successful')
        }

        if country_code is None:
            country = IBAN_SPCIFICATION_CONFIG[choice(list(IBAN_SPCIFICATION_CONFIG.keys()))]
        elif country_code in IBAN_SPCIFICATION_CONFIG.keys():
            country = IBAN_SPCIFICATION_CONFIG[country_code]
        else:
            result.update({
                'status'           : False,
                'generator_message': _('Invalid country code: {}').format (country)})
            return result

        result['bank'          ] = bank    if bank    else self.randomize_field(country.bank_specification   )
        result['account'       ] = account if account else self.randomize_field(country.account_specification)
        result['country_code'  ] = country.country_code

        try:
            result['generated_iban'] = self.calc_iban(country, result['bank'], result['account'])
        except Exception as e:
            result.update({
                'status'           : False,
                'generator_message': e.message})
        return result
