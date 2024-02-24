from django.shortcuts import render


def index_page(request):
    context = {
        'name':'GUEST'
    }
    return render(request, 'index.html', context)
