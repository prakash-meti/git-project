from django.shortcuts import render

# Create your views here.
def show_home_page(request):

    context = {
        'name':'Prakash'
    }
    return render(request, 'testapp/home.html', context)