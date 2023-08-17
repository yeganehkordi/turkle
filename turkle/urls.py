from django.urls import path

from .views import (
    accept_task,
    accept_next_task,
    task_assignment,
    task_assignment_iframe,
    index,
    help_page,
    preview,
    preview_iframe,
    preview_next_task,
    return_task_assignment,
    skip_and_accept_next_task,
    skip_task,
    stats_for_self,
    stats_for_user,
    update_auto_accept,
    user_activity_json,
    get_tasks
)

urlpatterns = [
    path('', index, name='index'),
    path('stats/', stats_for_self, name='stats'),
    path('stats/user/<int:user_id>/', stats_for_user, name='stats_for_user'),
    path('stats/user/<int:user_id>/activity.json', user_activity_json, name='user_activity_json'),
    path('help/', help_page, name='help'),
    path('update_auto_accept/', update_auto_accept, name='update_auto_accept'),
    path('get_tasks/', get_tasks, name='get_tasks'),
    path('task/<int:task_id>/', preview, name='preview'),
    path('task/<int:task_id>/iframe/', preview_iframe, name='preview_iframe'),
    path('task/<int:task_id>/assignment/<int:task_assignment_id>/return/',
         return_task_assignment, name='return_task_assignment'),
    path('task/<int:task_id>/assignment/<int:task_assignment_id>/',
         task_assignment, name='task_assignment'),
    path('task/<int:task_id>/assignment/iframe/<int:task_assignment_id>/',
         task_assignment_iframe, name='task_assignment_iframe'),
    path('batch/<int:batch_id>/accept_task/<int:task_id>/', accept_task, name='accept_task'),
    path('batch/<int:batch_id>/skip_task/<int:task_id>/', skip_task, name='skip_task'),
    path('batch/<int:batch_id>/skip_and_accept_next_task/<int:task_id>/<int:task_assignment_id>/',
         skip_and_accept_next_task, name='skip_and_accept_next_task'),
    path('batch/<int:batch_id>/accept_next_task/', accept_next_task, name='accept_next_task'),
    path('batch/<int:batch_id>/preview_next_task/', preview_next_task, name='preview_next_task'),
]
