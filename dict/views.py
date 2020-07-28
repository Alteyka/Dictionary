from django.shortcuts import render
from dict.models import Word
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import CreateWordForm


def home_page(request):
    template_name = 'home-page.html'
    return render(request, template_name)


def words_list(request):
    template_name = 'words.html'
    words = Word.objects.all()
    context = {'words': words}
    return render(request, template_name, context)


class CreateWord(View):
    form_class = CreateWordForm
    initial = {'key': 'value'}
    template_name = 'create-word.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/words/')
        return render(request, self.template_name, {'form', form})
