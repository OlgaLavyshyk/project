from .forms import InputModelForm, FileInput
from .parser.parser import Parser
from django.shortcuts import render

def home(request):
    if request.method == 'POST' and 'article' in request.POST:
        form = InputModelForm(request.POST, request.FILES)

        if form.is_valid():
            new_request = form.cleaned_data['article']
            print("start Parse", request.POST.get('article'))
            art = str(request.POST.get('article'))
            p = Parser()
            r = p.parse_single_article(art)

    else:
        form = InputModelForm()
    if request.method == 'POST' and 'file' in request.POST:
        file_form = FileInput(request.POST, request.FILES)
        # if file_form.isvalid:
        instance = FileInput(articles=request.FILES['file'])
        instance.save()


    else:
        file_form = FileInput()
    return render(request, 'home.html', {'form': form, 'table_form': file_form})

