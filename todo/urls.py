from django.urls import path

from todo.views import ToDoListView, TagListView, TagCreateView, TagUpdateView, TagDeleteView, ToDoCreateView, \
    ToDoUpdateView, ToDoDeleteView, change_progress_to_y, change_progress_to_n

urlpatterns = [
    path("", ToDoListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/create/", ToDoCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", ToDoUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", ToDoDeleteView.as_view(), name="task-delete"),
    path("tasks/change_to_y/<int:pk>/", change_progress_to_y, name="change-to-y"),
    path("tasks/change_to_n/<int:pk>/", change_progress_to_n, name="change-to-n"),
]

app_name = "todo"
