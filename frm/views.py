# Create your views here.
from django import forms;
from django.forms.formsets import formset_factory;
from django.shortcuts import render_to_response


class KeyValueForm(forms.Form):
  key = forms.CharField();
  value = forms.CharField();


def test(request):
    KeyValueFormSet= formset_factory(KeyValueForm, extra=1)
    if request.method == 'POST':
        print request.POST
        formset = KeyValueFormSet(request.POST)
        if formset.is_valid():
          for i in range(0, formset.total_form_count()):
            form = formset.forms[i]
            print form.cleaned_data;
    else:
        formset = KeyValueFormSet()
    return render_to_response('index.html', {'formset': formset})




