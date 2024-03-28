from django.shortcuts import render, redirect
from django.views import View


class StartPage(View):
    def get(self, request):
        return render(request, 'mydictionary/home_page.html')


def read_from_file(request):
    file = open("mydictionary/dictionary.txt", "r", encoding="utf-8").read().splitlines()
    words = []
    for line in file:
        word_en, word_rus = line.split(", ")
        words.append((word_en.split(": ")[1], word_rus.split(": ")[1]))
    return render(request, 'mydictionary/words_list.html', {"words": words})


def add_to_file(request):
    if request.method == 'GET':
        return render(request, 'mydictionary/add_word.html')

    else:
        print(request.POST)
        with open("/home/anton/PycharmProjects/django_learning/learn_django/mydictionary/dictionary.txt", "a",
                  encoding='utf-8') as file:
            file.writelines(f"\nword_1: {request.POST['word1']}, word_2: {request.POST['word2']}")
        return redirect(add_to_file)
