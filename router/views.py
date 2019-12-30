from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.views import View
from .models import *
from django.db.models import Avg
from django.core.exceptions import ObjectDoesNotExist
import random


class home(View):
    def get(self, request):
        restaurants = Restaurant.objects.all().only('name')
        choice = random.choice(restaurants)
        return HttpResponseRedirect("/restaurant/" + choice.name + "/")


class RestaurantInfoView(View):
    def get(self, request, name):
        info = Restaurant.objects.get(name=name)
        comments = CommentField.objects.filter(restaurant=info)
        score = comments.aggregate(Avg('grade'))
        categories = Category.objects.all()
        restaurants = Restaurant.objects.all().only('name', 'category')
        print(score)
        return render(request, 'index.html', {
            'info': info,
            'comments': comments,
            'score': round(score['grade__avg'], 2),
            'categories': categories,
            'restaurants': restaurants,
        })

    def post(self, request, name):
        try:
            info = Restaurant.objects.get(name=name)
        except ObjectDoesNotExist:
            return HttpResponseNotFound()
        if request.POST['type'] == "comment":
            post_type = "留言"
            if CommentPost(request, name, info) is False:
                return HttpResponseForbidden()
        elif request.POST['type'] == "suggestion":
            post_type = "建議"
            if SuggestionPost(request, name, info) is False:
                return HttpResponseForbidden()
        comments = CommentField.objects.filter(restaurant=info)
        score = comments.aggregate(Avg('grade'))
        categories = Category.objects.all()
        restaurants = Restaurant.objects.all().only('name', 'category')
        return render(request, 'index.html', {
            'info': info,
            'comments': comments,
            'score': score,
            'categories': categories,
            'restaurants': restaurants,
            'post_message': '已收到你的' + post_type
        })


def CommentPost(request, name, restaurant):
    receives = list()
    receives.append(request.POST.get('name', ''))
    receives.append(request.POST.get('grade', ''))
    receives.append(request.POST.get('comment', ''))
    if '' in receives:
        return False
    try:
        CommentField(
            name=receives[0],
            grade=receives[1],
            comment=receives[2],
            restaurant=restaurant
        ).save()
    except Exception:
        return False
    return True


def SuggestionPost(request, name, restaurant):
    receives = list()
    receives.append(request.POST.get('name', ''))
    receives.append(request.POST.get('email', ''))
    receives.append(request.POST.get('category', ''))
    receives.append(request.POST.get('comment', ''))
    if '' in receives:
        return False
    try:
        Suggestion(
            name=receives[0],
            email=receives[1],
            category=receives[2],
            comment=receives[3],
            restaurant=restaurant
        ).save()
    except Exception as e:
        print(e)
        return False
    return True
