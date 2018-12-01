from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . forms import contactFormed
from django.http import HttpResponseRedirect


# Create your views here


def index(request):
    return render(request, 'general/index.html')


def service(request):
    return render(request, 'general/service.html')


def about(request):
    return render(request, 'general/about.html')


def training(request):
    return render(request, 'general/training.html')


def gallery(request):
    return render(request, 'general/gallery.html')


"""def thanks(request):
    return render(request, 'general/contact/thanks.html')"""


class contactFormView(TemplateView):
    template_name = 'general/contactform.html'


def get_name(request):
    if request.method == 'POST':
        form = contactFormed(request.POST)
        if form.is_valid():
            form.save(commit=True)
            firstname = form.cleaned_data['First_name']
            lastname = form.cleaned_data['Last_name']
            sender = form.cleaned_data['sender']
            return index(request)
        else:
            print(form.errors)
    else:
        form = contactFormed()
        return render(request, 'contactform.html', form)

        # else:
        #    form = contactFormed()
        # return render(request, 'contactform.html', {'form': form})

    """def get(self, request):
        form = contactForms()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = contactForms(request.POST)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data['First_name']
            lastname = form.cleaned_data['Last_name']
            sender = form.cleaned_data['sender']

            return redirect('contactform:contactform')
        else:
            args = {'form': form}
            return render(request, self.template_name, args)"""
