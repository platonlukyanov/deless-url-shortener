import qrcode
import io
from django import forms
from django.core.files.base import ContentFile
from django.forms import ValidationError
from django.core.files.images import ImageFile
from .models import Link
from .utils import generate_code, image_to_byte_array, get_unique_code


class LinkCreateForm(forms.ModelForm):
    code = forms.CharField(required=False)
    domain = forms.URLField(widget=forms.HiddenInput())

    class Meta:
        model = Link
        fields = ('original',)

    def clean_code(self):
        previous_codes = Link.objects.values_list('shorted_link_code', flat=True)
        code = self.cleaned_data["code"]
        if code in previous_codes:
            raise ValidationError("Указанная ссылка не уникальна")
        return code

    def save(self, commit=True):
        # Setting Short Link Code
        previous_codes = Link.objects.values_list('shorted_link_code', flat=True)
        if not self.cleaned_data.get("code"):
            # if user missed custom code field
            print("user missed code")
            code = get_unique_code(generate_code, previous_codes)
        else:
            code = self.cleaned_data["code"]

        new_link = super().save(commit=False)
        new_link.shorted_link_code = code
        short_url = self.cleaned_data.get("domain") + "/" + code

        # Creating QR

        qr_obj = qrcode.make(short_url)  # Creating QR Object
        pil_qr_img = qr_obj.get_image()  # Getting PIL Image
        bytes_arr = image_to_byte_array(pil_qr_img)  # Converting PIL Image to bytes

        # Setting QR image to Django Field
        new_link.qr.save('{}.png'.format(code), ContentFile(bytes_arr), save=False)

        # Creating Secret Key for Access to Statistics
        previous_secret_link_keys = Link.objects.values_list('secret_key', flat=True)
        secret_link_key = get_unique_code(generate_code, previous_secret_link_keys, start_length=4)
        new_link.secret_key = secret_link_key

        # Final Actions
        if commit:
            new_link.save()
        return new_link
