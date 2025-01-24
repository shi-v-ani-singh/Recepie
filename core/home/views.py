from django.shortcuts import render

# Create your views here.
# (all logics)
from django.http import HttpResponse

def home(request):
    # return HttpResponse('''<h1>Hey, i am django server.</h1>
    #                     <p> this is a paragraph</P>''')
    # # this upper way of html is not feasible to write like this
    peoples=[
        {'name':'shivani','age':23},
         {'name':'sakshi','age':20},
         {'name':'kaju','age':22}
    ]
    text='''Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo inventore nemo esse tempora fugit assumenda maxime consequatur facilis error eum mollitia consectetur minus, deserunt eligendi! Quae rem iusto dolor possimus!'''
    for people in peoples:
        print(people)
        
    return render(request, 'index.html', context={'peoples':peoples,'text':text})
def about(request):
    context={'page':'about'}
    return render(request, 'about.html')

def contact(request):
    context={'page':'contact'}
    return render(request, 'contact.html')

def success_page(request):
    
    # print("*"*10) #this is logic
    return HttpResponse('<h1> hey this is a success page.</h1>')