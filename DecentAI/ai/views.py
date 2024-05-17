from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ai.forms import ai_form
from ai.ai import ChatCompletion
import json

def ai(request):
    if request.method == "POST":
        response_data = json.loads(request.body)
        print(response_data['formData']['data'])
        ai = ChatCompletion()
        answer = ai.question(response_data['formData']['data'])
        return JsonResponse(json.dumps(answer), safe=False)
    form = ai_form
    return render(request, 'ai_home.html', {'form': form})
