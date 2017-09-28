from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from random import choice
from vocabulary.models import Word
import json

const = 20

def index(request):
	if request.method == 'POST':
		body_decode = request.body.decode('utf-8')
		body_data = json.loads(body_decode)
		word = Word.objects.all().filter(id=body_data['word_id'])[0]
		word.correct_count = word.correct_count + 1
		word.save()
		return HttpResponse()
	return render(request, 'index.html')

def new(request):
	rand = weighted_random()
	word = Word.objects.all()[rand]
	word.all_count = word.all_count + 1 ;
	word.save() ;
	return JsonResponse({'prob': word.prob, 'ans': word.ans, 'word_id': word.id})

def add(request):
	return render(request, 'add.html')

def data(request):
	if request.method == 'POST':
		body_decode = request.body.decode('utf-8')
		body_data = json.loads(body_decode)
		Word.objects.create(prob = body_data['prob'], ans = body_data['ans'])
		return HttpResponse()
	elif request.method == 'DELETE':
		body_decode = request.body.decode('utf-8')
		body_data = json.loads(body_decode)
		Word.objects.filter(id=body_data['word_id']).delete()
		return HttpResponse()
	return HttpResponse(status=500)
	

def show_problemset(request):
	return render(request, 'show.html', {
		'words': Word.objects.all()
	})


def weighted_random():
	weighted_list = []
	for i in range(Word.objects.count()):
		weight = int(const/(Word.objects.all()[i].correct_count+1))
		weighted_list.extend([i]*weight)
	return choice(weighted_list)

