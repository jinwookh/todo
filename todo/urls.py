from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name = 'index'),
    #from start -> this path -> views.index -> index.html
    path('<int:todo_id>', views.detail, name = 'detail'),
    #from index.html -> this path -> views.detail -> detail.html
    path('<int:todo_id>/check_complete/', views.checkComplete, name = 'check'),
    #from detail.html -> this path -> views.checkComplete -> index.html
    path('<int:todo_id>/editor/', views.adjust, name = 'adjust'),
    #from detail.html -> this path -> views.adjust -> adjust.html
    path('<int:todo_id>/notice_for_deletion/', views.delete, name = 'delete'),
    #from detail.html -> this path -> views.deletion -> delete.html
    path('finished_List/', views.finishedList, name = 'finished'),
    #from index.html -> this path -> views.finishedList ->finishedList.html
    path('register/', views.create, name = 'create'),
    #from index.html -> this path -> views.create -> create.html
    path('notice_for_creation/', views.creation, name = 'creation'),
    #from create.html -> this path -> views.creation -> creation.html
    path('notice_for_adjustment/', views.adjustment, name = 'adjustment'),
    #from adjust.html -> this path -> views.adjustment -> adjustment.html
]
