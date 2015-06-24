from django.forms            import ModelForm
from django.forms            import FileInput
from django.contrib          import admin
from easy_thumbnails.files   import get_thumbnailer
from django.utils.safestring import mark_safe

from user_management.models import UserInformation


class AdminImageWidget(FileInput):
    def __init__(self, attrs={}):
        FileInput.__init__(self, attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            preview_url = get_thumbnailer(value)['preview'].url
            output.append("""
                <a target="_blank" href="{}">
                    <img src="{}" class="admin_preview"/>
                </a>
                """.format(value.url, preview_url))
        output.append(FileInput.render(self, name, value, attrs))
        return mark_safe(u''.join(output))


class UserInformationAdminForm(ModelForm):
    class Media:
        css = {
            'all': ('css/styles.css',)
        }

    class Meta:
        model   = UserInformation
        fields  = ['picture', 'first_name', 'last_name', 'IBAN_account', 'account_manager']
        widgets = {
            'picture': AdminImageWidget
        }


class UserInformationAdmin(admin.ModelAdmin):
    form          = UserInformationAdminForm
    list_filter   = ['IBAN_account', 'first_name', 'last_name',                          ]
    list_display  = ['IBAN_account', 'first_name', 'last_name', 'admin_picture_thumbnail']


admin.site.register(UserInformation, UserInformationAdmin)
