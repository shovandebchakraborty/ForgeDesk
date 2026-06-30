from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def ProjectCreateAPI(request):
    data = json.loads(request.body)

    if request.method == 'POST':
        projectIcon = data.get('icon')
        projectName = data.get('projectName')
        projectDescription = data.get('Description')

        ProjectStructure.objects.create(
            Icon = projectIcon,
            Name = projectName,
            Description = projectDescription
        )

        DataResponse = []
        for get in ProjectStructure.objects.all():
            DataResponse.append(get.Name)

        return JsonResponse({
            "Project-status" : "Done",
            "Project-Name" : DataResponse,
            "Message" : "Uploaded"
        })
