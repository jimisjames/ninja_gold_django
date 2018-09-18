from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):

    if not 'gold' in request.session.keys():
        request.session['gold'] = 0

    if not 'activity' in request.session.keys():
        request.session['activity'] = ["Welcome to Ninja Gold!"]

    return render(request, "gold/index.html")


def process_gold(request, data):

    if data == "farm":
        gold = random.randint(10,21)
    elif data == "cave":
        gold = random.randint(5,11)
    elif data == "house":
        gold = random.randint(2,6)
    elif data == "casino":
        gold = random.randint(-50,51)
    elif data == "reset":
        request.session.clear()
        return redirect("/")

    request.session['gold'] += gold 

    temp = request.session['activity']
    temp.reverse()
    if gold < 0:
        temp.append("You lost "+str(gold)+" gold, oh no!")
    else:
        temp.append("You earned "+str(gold)+" gold!")
    temp.reverse()
    request.session['activity'] = temp


    if request.session['gold'] < 0:
        temp = request.session['activity']
        temp.reverse()
        temp.append("You are in debt to the mob! They are coming for you!")
        temp.reverse()
        request.session['activity'] = temp


    return redirect("/")
