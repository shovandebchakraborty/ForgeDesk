from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
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
    return JsonResponse({
        "status" : "Not yet",
        "Message" : "Not uploaded yet"
    })

# This API will show all details of Projects 
def ProjectViewAPI(request):
    Data = []

    if request.method == 'GET':
        for get in ProjectStructure.objects.all():
            project_structre_data = model_to_dict(get)
            Data.append(project_structre_data)
        
        return JsonResponse({
            "Status" : True,
            "Number Of Projects": len(Data),
            "Title of Project" : Data
        }, status=200)
    else:
        return JsonResponse({
            "Status" : "Not Yet",
            "Message" : "Not data yet"
        }, status=405)