from django import template
from django.conf import settings
from django.forms.forms import BaseForm
from django.forms.fields import (CharField, EmailField)

register = template.Library()

DATA_MASKER_DEFAULT_CLEAR_HEADING = 2
DATA_MASKER_DEFAULT_CLEAR_TAILING = 2
DATA_MASKER_DEFAULT_FIELD_LIST = [
    'account_name',
    'account_number',
    'bank',
    'branch',
    'email',
]

class BaseMasker(object):
    """
    A content masker
    """
    def __init__(self, *args, **kwargs):
        pass

    def _mask(self):
        return None

    def mask(self):
        return self._mask()

class FormMasker(BaseMasker):
    clear_heading  = getattr(
        settings, 'DATA_MASKER_CLEAR_HEADING', DATA_MASKER_DEFAULT_CLEAR_HEADING)

    clear_tailing = getattr(
        settings, 'DATA_MASKER_CLEAR_TAILING', DATA_MASKER_DEFAULT_CLEAR_TAILING)

    field_list = getattr(
        settings, 'DATA_MASKER_FIELD_LIST', DATA_MASKER_DEFAULT_FIELD_LIST)

    def __init__(self, form, *args, **kwargs):
        if not isinstance(form, BaseForm):
            raise Exception('Parameter "form" should contain a valid Django Form.')

        self.form = form
        self.clear_text_count = self.clear_heading + self.clear_tailing

        super(FormMasker, self).__init__(*args, **kwargs)

    def mask_string(self, value):
        str_len = len(value)

        if str_len > self.clear_text_count:
            return "{}{}{}".format(
                value[:self.clear_heading],
                '*' * (str_len - self.clear_text_count),
                value[-self.clear_tailing:])
        else:
            return '*' * str_len

    def mask_email(self, value):
        username, domainname = value.split('@')

        return "{}@{}".format(
            self.mask_string(username),
            domainname)

    def mask_fields(self):
        for field_name in self.field_list:
            if not field_name in self.form.initial:
                continue

            original_value = self.form.initial[field_name]
            field_type = type(self.form.fields[field_name])

            if field_type is CharField:
                new_value = self.mask_string(original_value)
            elif field_type is EmailField:
                new_value = self.mask_email(original_value)

            self.form.initial[field_name] = new_value

    def _mask(self):
        self.mask_fields()

        return self.form

@register.simple_tag
def mask_form(*args, **kwargs):
    return FormMasker(*args, **kwargs).mask()

