from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse 
from .utils import predict_sentiment
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , get_object_or_404 ,redirect
from django.urls import reverse
from django.utils import timezone
from .models import User , Course , UserCourse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courtera/courses.html', {'courses': courses
                                                     })

@login_required
def my_courses(request):
    if request.method == "POST":
        course_id = request.POST.get("course_id")
        action = request.POST.get("action")  # "add" or "remove"
        course = get_object_or_404(Course, id=course_id)

        if action == "add":
            if UserCourse.objects.filter(user=request.user, course=course).exists():
                messages.warning(request, "You already added this course.")
            else:
                UserCourse.objects.create(user=request.user, course=course)
                messages.success(request, f"'{course.title}' added to your courses.")

        elif action == "remove":
            deleted, _ = UserCourse.objects.filter(user=request.user, course=course).delete()
            if deleted:
                messages.success(request, f"'{course.title}' removed from your courses.")
            else:
                messages.warning(request, "This course was not in your list.")

        return redirect("my_courses")

    # For GET requests: show all courses and user's added courses
    courses = Course.objects.all()
    user_courses = UserCourse.objects.filter(user=request.user).select_related("course")
    user_course_ids = user_courses.values_list("course_id", flat=True)

    return render(
        request,
        "courtera/my_courses.html",
        {
            "courses": courses,
            "user_course_ids": user_course_ids,
            "user_courses": user_courses,
            "user": request.user,
        },
    )
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    prediction = None

    if request.method == "POST":
        text = request.POST.get("text", "")
        if text:
            prediction = predict_sentiment(text)

    return render(request, "courtera/course_detail.html", {
        "course": course,
        "prediction": prediction
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("course_list"))
        else:
            return render(request, "courtera/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "courtera/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "courtera/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("course_list"))
    else:
        return render(request, "courtera/register.html")
