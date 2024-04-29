from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [

    # READ
    # path('', views.index, name='index'),
    # path('bugs/', views.bugs_list, name='bugs_list'),
    # path('features/', views.features_list, name='features_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('features/<int:feature_id>/', views.feature_id_detail, name='feature_detail'),

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugsListView.as_view(), name='bugs_list'),
    path('features/', views.FeaturesListView.as_view(), name='features_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),

    #CREATE
    # path('bugs/new/', views.add_bug_report, name='bug_report_form'),
    # path('features/new/', views.add_feature_request, name='feature_list_form'),

    path('bugs/new/', views.BugCreateView.as_view(), name='bug_report_form'),
    path('features/new/', views.FeatureCreateView.as_view(), name='feature_list_form'),

    # UPDATE
    # path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    # path('features/<int:feature_id>/update/', views.update_feature, name='update_feature'),

    path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug'),
    path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='update_feature'),

    # DELETE
    # path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    # path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),

    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
]


