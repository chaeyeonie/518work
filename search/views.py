#from selenium import webdriver
#from selenium.webdriver.common.keys import keys
from time import sleep
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from .forms import SearchingForm

# Create your views here.
def enter(request):
    if request.method == "POST":
        form = SearchingForm(request.GET)
        
        if form.is_valid():
            query = (form.cleaned_data['query'])
            return redirect('engine', query)
    else:
        form = SearchingForm()    
        return render(request, 'enter.html', {'form':form})

def result(request):
    URL = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
    query = request.GET.get('search_term', '')
    fullURL = URL + query
    html = requests.get(fullURL).text
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find_all(class_='_sp_each_title')
    
    title_array = []
    for title in news_title:
        title_array.append({'url':title.get('href'), 'title':title.get('title')})
    return render(request, 'result.html', {'title_array': title_array})

def engine(request, query):
  title_array = result(query)
  return render(request, 'enter.html', {'query':query, 'title_array':title_array})