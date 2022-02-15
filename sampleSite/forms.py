"""
    form.py
"""
from django.core.files.storage import default_storage
from django import forms

class IndexForm(forms.Form):
    message = forms.CharField(
        label = "kweet",
        max_length=200,
        required=True
    )

    suuji = forms.IntegerField(
        required=False
    )
    
    choice = forms.ChoiceField(
        widget=forms.Select,
        choices=(
            ("図１","図１"),
            ("図２","図２")
        )
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={"type":"date"}),
        input_formats=['%Y-%m-%d']
    )

    chk = forms.BooleanField(
        widget=forms.CheckboxInput
    )

    opt = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(
            ("OPT1","OPT1"),
            ("OPT2","OPT2")
        )
    )


class Application1Form(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()
    sisoku = forms.ChoiceField(
        widget=forms.Select,
        choices=(
            ("+","+"),
            ("-","-"),
            ("*","*"),
            ("/","/")
        )
    )

class Application2Form(forms.Form):
    text = forms.CharField()

class Application4Form(forms.Form):
    gazou = forms.FileField()
    def save(self):
        upload_file = self.cleaned_data['gazou']
        file_name = default_storage.save(upload_file.name,upload_file)
        return default_storage.url(file_name)

class KakeiboForm(forms.Form):
    message = forms.CharField(
        max_length=200,
        required=True
    )
    suuji = forms.IntegerField(
        required=False
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type":"date"}),
        input_formats=['%Y-%m-%d']
    )
    opt = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(
            ("収入","収入"),
            ("支出","支出"),
            ("借金","借金")
        )
    )


