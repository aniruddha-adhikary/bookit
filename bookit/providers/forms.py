from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div
from django.forms import Form


class SearchForm(Form):
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
