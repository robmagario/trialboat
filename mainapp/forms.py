from django import forms
from django.contrib.auth.models import User
from django.forms import CheckboxInput, SelectMultiple
from django.utils.encoding import force_text
from django.utils.html import escape
from django.utils.safestring import mark_safe

from mainapp.models import Customer


class TableSelectMultiple(SelectMultiple):
    def __init__(self, item_attrs, *args, **kwargs):
        super(TableSelectMultiple, self).__init__(*args, **kwargs)
        self.item_attrs = item_attrs

    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = []
        has_id = attrs and 'id' in attrs
        final_attrs = self.build_attrs(attrs, name=name)
        output = []
        str_values = set([force_text(v) for v in value])  # Normalize to strings.
        for i, (option_value, item) in enumerate(self.choices):
            if has_id:
                final_attrs = dict(final_attrs, id='%s_%s' % (attrs['id'], i))
            cb = CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
            option_value = force_text(option_value)
            rendered_cb = cb.render(name, option_value)
            output.append(u'<tr><td>%s</td>' % rendered_cb)
            for attr in self.item_attrs:
                if callable(attr):
                    content = attr(item)
                elif callable(getattr(item, attr)):
                    content = getattr(item, attr)()
                else:
                    content = getattr(item, attr)
                output.append(u'<td>%s</td>' % escape(content))
            output.append(u'</tr>')
        return mark_safe(u'\n'.join(output))

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("address", 'zip', 'city', 'country')


class SelectProductForm(forms.Form):
    products = forms.MultipleChoiceField(widget=TableSelectMultiple(item_attrs=('description', 'weight')))

    def __init__(self, products_data, *args, **kwargs):
        super(SelectProductForm, self).__init__(*args, **kwargs)
        self.fields['products'].choices = [(p.id, p) for p in products_data]