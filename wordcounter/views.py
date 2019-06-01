from django.shortcuts import render 
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split() #전체 텍스트를 스페이스로 나눔
    word_dic = {} #사전형 변수

    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else :
            word_dic[word] = 1

    return render(request, 'count.html', {'fulltext' : full_text,
                                        'total' : len(word_list),
                                        'dictionary' : word_dic.items()})

def select(request):
    #로또번호 추출 코드
    list = []
    ran_num = random.randint(1,45)

    for i in range(6):
        while ran_num in list:
            ran_num = random.randint(1, 45)
        list.append(ran_num)

    list.sort()

    return render(request, 'home.html', {'list':list}) #(3) list의 값을 'list'라는 이름으로 보낸다.