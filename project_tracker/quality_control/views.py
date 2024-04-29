from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import BugReport, FeatureRequest
from tasks.models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.views import View
from .forms import BugReportForm, FeatureRequestForm
from django.views.generic.edit import UpdateView, DeleteView



def index(request):
    return render(request, 'quality_control/index.html')


# def index(request):
#     bugs_url = reverse('quality_control:bug_list')
#     feature_url = reverse('quality_control:feature_list')
#     html = f'''
#     <h1>Система контроля качества</h1>
#     <ul>
#         <li>
#             <a href='{bugs_url}'>Список всех багов</a>
#         </li>
#         <li>
#             <a href='{feature_url}'>Запросы на улучшение</a>
#         </li>
#     </ul>
# '''
#     return HttpResponse(html)


def bugs_list(request):
    bug = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs_list': bug})

# def bug_list(request):
#     bugs = BugReport.objects.all()
#     bugs_html = '<h1>Список всех багов</h1><ul>'
#     for bug in bugs:
#         bugs_html += f'''
#         <li>
#             <a href="{bug.id}/">{bug.title}</a>
#             <br>
#             <pre>  Status: {bug.status}</pre>
#         </li>
#         '''
#     bugs_html += '</ul>'
#     return HttpResponse(bugs_html)


def features_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'features_list': features})


# def feature_list(request):
#     features = FeatureRequest.objects.all()
#     features_html = '<h1>Список всех запросов на улучшение</h1><ul>'
#     for feature in features:
#         features_html += f'''
#             <li>
#                 <a href="{feature.id}/">{feature.title}</a>
#                 <br>
#                 <pre>  Status: {feature.status}</pre>
#             </li>
#             '''
#     features_html += '</ul>'
#     return HttpResponse(features_html)


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def feature_id_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         bugs_url = reverse('quality_control:bug_list')
#         feature_url = reverse('quality_control:feature_list')
#         html = f'''
#             <h1>Система контроля качества</h1>
#             <ul>
#                 <li>
#                     <a href='{bugs_url}'>Список всех багов</a>
#                 </li>
#                 <li>
#                     <a href='{feature_url}'>Запросы на улучшение</a>
#                 </li>
#             </ul>
#         '''
#         return HttpResponse(html)


class BugsListView(ListView):
    model = BugReport
    context_object_name = "bugs_list"
    template_name = 'quality_control/bugs_list.html'


class FeaturesListView(ListView):
    model = FeatureRequest
    context_object_name = "features_list"
    template_name = 'quality_control/features_list.html'


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = "bug"
    template_name = 'quality_control/bug_detail.html'


# class BugDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         bug = self.object
#         response_html = f'''
#         <h1><pre><strong>Title:</strong>  {bug.title}</pre></h1>
#         <p>
#             <pre><strong>Description:</strong> {bug.description}</pre>
#         </p>
#         <p>
#             <pre><strong>Status:</strong>  {bug.status}</pre>
#         </p>
#         <p>
#             <pre><strong>Priority:</strong>  {bug.priority}</pre>
#         </p>
#         <p>
#             <pre><strong>Находится в проекте:</strong>  {bug.project}</pre>
#         </p>
#         <p>
#             <pre><strong>Относится к задаче:</strong>  {bug.task}</pre>
#         </p>
#         '''
#         return HttpResponse(response_html)


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = "feature"
    template_name = 'quality_control/feature_detail.html'


# class FeatureDetailView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         feature = self.object
#         response_html = f'''
#         <h1><pre><strong>Title:</strong>  {feature.title}</pre></h1>
#         <p>
#             <pre><strong>Description:</strong> {feature.description}</pre>
#         </p>
#         <p>
#             <pre><strong>Status:</strong>  {feature.status}</pre>
#         </p>
#         <p>
#             <pre><strong>Priority:</strong>  {feature.priority}</pre>
#         </p>
#         <p>
#             <pre><strong>Находится в проекте:</strong>  {feature.project}</pre>
#         </p>
#         <p>
#             <pre><strong>Относится к задаче:</strong>  {feature.task}</pre>
#         </p>
#         '''
#         return HttpResponse(response_html)


def add_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def add_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bugs_list')


class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:features_list')


def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_report_update.html', {'form': form, 'bug': bug})


def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_request_update.html', {'form': form, 'feature': feature})


class BugUpdateView(DetailView, UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_update.html'
    pk_url_kwarg = 'bug_id'

    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail', kwargs={'bug_id': self.object.id})


class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_update.html'
    pk_url_kwarg = 'feature_id'

    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail', kwargs={'feature_id': self.object.id})


def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bugs_list')


def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:features_list')


class BugDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = "bug"
    success_url = reverse_lazy('quality_control:bugs_list')
    template_name = 'quality_control/bug_confirm_delete.html'


class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = "feature"
    success_url = reverse_lazy('quality_control:features_list')
    template_name = 'quality_control/feature_confirm_delete.html'
