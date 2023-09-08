from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
# Create your views here.
def endpoint(request):
 slack_name = request.GET.get('slack_name', 'Olayimika Kayode')
 track = request.GET.get('track', 'Backend')
 current_date=datetime.now()
 current_time=current_date.strftime('%H:%M:%S')
 data = {'message':'This is my api',
         "Slack_name":slack_name,
         "Current_day":f"{current_date.strftime('%A')}",
         "utc_time":f"{current_time}",
         "track":track,
         "gitbub_file_url":"https://github.com/0layimika/endpoint_project/tree/main/endpoint",
         "github_repo":"https://github.com/0layimika/endpoint_project",
         "status_code":200}
 return JsonResponse(data)
