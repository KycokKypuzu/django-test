from django.http import HttpResponse
from django.urls import reverse


def index(request):
    bugs_url = reverse('quality_control:bug_list')
    feature_url = reverse('quality_control:feature_list')
    html = f'''
    <h1>Система контроля качества</h1>
    <ul>
        <li>
            <a href='{bugs_url}'>Список всех багов</a>
        </li>
        <li>
            <a href='{feature_url}'>Запросы на улучшение</a>
        </li>
    </ul>
'''
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse("Список отчётов об ошибках")

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_id_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")
