from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Student, Course, Category, Instructor, Order


# Create your views here.
def index(request):
    category_list = Category.objects.all().order_by("id")[:10]
    course_list = Course.objects.all().order_by("-price")[:5]
    order_list = Order.objects.all().order_by("-order_date")[:5]
    ins_list = Instructor.objects.all()[:5]

    return render(
        request,
        "myappF23/index.html",
        {
            "course_list": course_list,
            "category_list": category_list,
            "order_list": order_list,
            "ins_list": ins_list,
        },
    )


def main_detail(request):
    category_list = Category.objects.all().order_by("id")[:10]
    ins_list = Instructor.objects.all()[:5]

    return render(
        request,
        "myappF23/detail.html",
        {
            "category_list": category_list,
            "ins_list": ins_list,
        },
    )


def about(request):
    return render(request, "myappF23/about.html")


def detail(request, category_no):
    category_name = get_object_or_404(Category, pk=category_no)
    course_list = Course.objects.filter(categories=category_no).order_by("id")

    return render(request, "myappF23/category_detail.html", {"course_list": course_list})


def instructor_detail(request, instructor_no):
    instructor_name = get_object_or_404(Instructor, pk=instructor_no)
    course_list = Course.objects.filter(instructor=instructor_no)

    stu_course_lst = []

    for course in course_list:
        students = []
        for st in course.students.all():
            students.append(st)

        stu_course = {"name": course.title, "students": tuple(students)}

        stu_course_lst.append(stu_course)

    # print(stu_course_lst)

    return render(
        request,
        "myappF23/ins_detail.html",
        {"instructor_name": instructor_name, "course_list": stu_course_lst},
    )


def students_by_ins(request, ins_no):
    ins = get_object_or_404(Instructor, pk=ins_no)
    students = ins.student.all()

    return render(
        request,
        "myappF23/stu_by_ins.html",
        {"st_list": students},
    )


def courses(request):
    courist = Order.objects.all().orderby('id')
    return render(request, 'myappF23/courses.html', {'courlist': courist})

def history(request, st_id):
    order = Order.objects.filter(student=st_id)
    # course1 = students.course.all()
    return render(request,"myappF23/stu_by_ins.html",{"course_list": order})