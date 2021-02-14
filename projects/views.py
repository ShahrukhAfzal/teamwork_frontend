import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from teamwork_frontend.config import ROOT_API_URL


def ListProjects(request):

    r = requests.get(ROOT_API_URL + 'project-app/projects/')
    project_list_data = r.json()
    next_page = project_list_data.get('next')
    prev_page = project_list_data.get('previous')
    count = project_list_data.get('count')
    results = project_list_data.get('results')

    context = {
        'projects': results,
        'next_page': next_page,
        'prev_page': prev_page,
        'count': count,
        }

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

    return redirect('list-project')


def EditProject(request, id):

    if request.method == 'GET':
        r = requests.get(ROOT_API_URL + f'project-app/projects/{id}')
        project_data = r.json()
        return render(request, 'projects/edit.html', context=project_data)
    else:
        updated_data = {
                'name': request.POST['name'],
                'description': request.POST['description']
            }
        r = requests.put(ROOT_API_URL + f'project-app/projects/{id}/', data=updated_data)
        return redirect('list-project')
