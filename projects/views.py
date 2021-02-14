import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from teamwork_frontend.config import ROOT_API_URL


def ListProjects(request):
    r = requests.get(ROOT_API_URL + 'project-app/projects/')
    project_list = r.json()
    print(project_list)
    context = {'message': 'success', 'projects': project_list}
    return render(request, 'projects/list.html', context=context)


def CreateProject(request):
    if request.method == 'GET':
        return render(request, 'projects/create.html')
    else:
        name = request.POST['name']
        description = request.POST['description']

        context = {
            'name': name,
            'description': description
        }

        r = requests.post(ROOT_API_URL + 'project-app/projects/', data=context)

        return redirect('list-project')


def DeleteProject(request, id):
    r = requests.delete(ROOT_API_URL + f'project-app/projects/{id}/')
    # if r.status == '404':
    #     context = {'message': 'No such object exists.'}
    # elif r.status == '200':
    #     context = {'message': 'Object deleted successfully.'}

    return redirect('list-project')

