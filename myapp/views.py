from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import operator
# Create your views here.
def index(request):
    return render(request,'home.html',{'name':'hii Gaurav Shrivastav'})
    # text = """<h1>welcome to my app index page!</h1>"""
    # return HttpResponse(text)
def count(request):
    data = request.GET['fulltextarea']#Get data from textarea countdetail
    word_list = data.split()
    # print(word_list)
    str_length = len(word_list)    
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:#check if word in the dic then increase the count
            word_dictionary[word] += 1
        else:                       # if word not in dic then add in to dictionary
            word_dictionary[word] = 1
    sorted_list = sorted(word_dictionary.items(),key = operator.itemgetter(1),reverse=True)
    print(sorted_list)
    return render(request,'countdetail.html',{'fulltext':data,'words':str_length,'word_dictionary':sorted_list})

def contact(request):
    text="""<h1><a href="http://127.0.0.1:8000/aboutus/">Hi this is contact page!</a></h1>"""
    return HttpResponse(text)  
def about_us(request):
    return render(request,'about.html')