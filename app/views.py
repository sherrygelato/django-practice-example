from django.shortcuts import render

import random

# 함수형으로 만들기!!

# 함수를 정의하는 경우 항상 첫번째 인자를 request로 정의한다.
# return은 항상 render로 작성한다. 
# render를 request 하는데 index.html 파일의 정보를 반환하겠다는 뜻이다.

# 함수를 지정하고 html로 갈 수 있게 설정한다.
# url에서 적은 이름으로 만들어야 한다.

def index(request):
    return render(request, 'index.html')

def lotto(request):
    pick = random.sample(range(1,46), 6)
    context = {
        'pick' : pick
    }
    return render(request, 'lotto.html', context)

# render() 안에는 request, 파일이름, 파일에 들어갈 변수 순
# context는 항상 dic

def computer(request):
    languages = ['HTML', 'CSS', 'Bootstrap', 'Django', 'Python']
    language = random.choice(languages)
    context = {
        'language' : language,
        'languages' : languages
    }
    return render(request, 'computer.html', context)

def hi(request, name):
    context = {
        'name' : name
    }
    return render(request, 'hi.html', context)

# def hi(request, name):
#    return render(request, 'hi.html', {'name':name}) 으로 할 수 있음
# 무조건 key:value 형태로 

def add(request, a, b):
    result = a + b
    context = {
        'result' : result
    }
    return render(request, 'add.html', context)

def posts(request, id):
    content = 'Life is short, you need python!'
    replies = ['유익하당', '별로당', '많은 정보 알아갑니다']
    no_replies = []
    user = 'sherry'
    context = {
        'id' : id,
        'replies' : replies,
        'no_replies' : no_replies,
        'content' : content,
        'user' : user,
    }
    return render(request, 'posts.html', context)
