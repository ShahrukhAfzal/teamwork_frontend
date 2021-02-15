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
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        context = {
            'name': name,
            'description': description,
            'start_date': start_date,
            'end_date': end_date,
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
        return redirect('detail-project', id=id)


def DetailProject(request, id):
    if request.method == 'GET':
        r = requests.get(ROOT_API_URL + f'project-app/projects/{id}/')
        project_data = r.json()
        return render(request, 'projects/detail.html', context=project_data)


def CreateTask(request, id):
    if request.method == 'GET':
        return render(request, 'tasks/create.html', context={'id': id})
    elif request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        context = {
            'name': name,
            'description': description,
            'project': id
        }

        r = requests.post(ROOT_API_URL + 'project-app/tasks/', data=context)
        return redirect('detail-project', id=id)


def DetailTask(request, project_id, task_id):
    if request.method == 'GET':
        r = requests.get(ROOT_API_URL + f'project-app/tasks/{task_id}/')
        task_data = r.json()
        task_data['project_id'] = project_id

        return render(request, 'tasks/detail.html', context=task_data)


def EditTask(request, project_id, task_id):
    if request.method == 'GET':
        r = requests.get(ROOT_API_URL + f'project-app/tasks/{task_id}/')
        task_data = r.json()
        task_data['project_id'] = project_id
        return render(request, 'tasks/edit.html', context=task_data)
    else:
        updated_data = {
                'name': request.POST['name'],
                'description': request.POST['description']
            }
        updated_data['project'] = project_id
        r = requests.put(ROOT_API_URL + f'project-app/tasks/{task_id}/', data=updated_data)
        return redirect('detail-project', id=project_id)


def DeleteTask(request, project_id, task_id):
    r = requests.delete(ROOT_API_URL + f'project-app/tasks/{task_id}/')

    return redirect('detail-project', id=project_id)
