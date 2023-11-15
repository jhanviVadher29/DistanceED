from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("stu_by_ins/<int:ins_no>", views.students_by_ins, name="students_by_ins"),
    path("<int:category_no>", views.detail, name="category_detail"),
    path("myappF23/about/", views.about, name="about"),
    path("detail/", views.main_detail, name="detail"),
    path("ins/<int:instructor_no>", views.instructor_detail, name="ins_detail"),
    path("history/<int:st_id>",views.history, name = "history")
    # path("corses/", views.courses(), name="courses")
]
