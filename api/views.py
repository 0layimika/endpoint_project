from django.shortcuts import render
from datetime import datetime, timezone
from django.http import JsonResponse
# Create your views here.
def endpoint(request):
 slack_name = request.GET.get('slack_name', 'Olayimika Kayode')
 track = request.GET.get('track', 'Backend')
 current_date=datetime.now(timezone.utc)
 data = {'message':'This is my api',
         "slack_name":slack_name,
         "current_day":f"{current_date.strftime('%A')}",
         "utc_time":f"{current_date.isoformat()}",
         "track":track,
         "github_file_url":"https://github.com/0layimika/endpoint_project/tree/main/endpoint",
         "github_repo_url":"https://github.com/0layimika/endpoint_project",
         "status_code":200}
 return JsonResponse(data)
