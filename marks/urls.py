from django.urls import path, re_path

from . import stu_views, marks_views

urlpatterns = [
    # path('/', stu_views.index, name='index'),

    path('/sturec', stu_views.StuView.as_view()),
    path('/total', marks_views.MarksTotal.as_view()),
    path('/avg', marks_views.MarksAvg.as_view()),
    # path('/details', stu_views.StuView.as_view()),
    re_path(r'^/(?P<stu_id>[0-9]+)/addmarks$', marks_views.MarksView.as_view()),
]