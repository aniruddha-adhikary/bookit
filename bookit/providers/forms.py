from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div, Submit
from django import forms

from providers.models import Provider, ProviderService


class SearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'

        self.helper.layout = Layout(
            Row(
                Div('name', css_class='col-sm-3'),
                Div('area', css_class='col-sm-3'),
            )
        )


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ('name', 'area')

    def save(self, commit=True):
        self.instance.owner = self._owner
        return super().save(commit)

    def __init__(self, *args, **kwargs):
        self._owner = kwargs.pop('owner')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Save Provider'))


class ProviderServiceForm(forms.ModelForm):
    class Meta:
        model = ProviderService
        fields = ('name', 'short_description', 'price', 'time_required')

    def save(self, commit=True):
        self.instance.provider = self._provider
        return super().save(commit)

    def __init__(self, *args, **kwargs):
        self._provider = kwargs.pop('provider')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Save Service'))
