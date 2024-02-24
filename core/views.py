from django.shortcuts import render


def index_page(request):
    context = {
        'name':'guest'
    }
    return render(request, 'index.html', context)