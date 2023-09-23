from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Length
# Create your views here.

def home(request):
    blogs = Blog.objects.filter(hidden=False)
    categories = Category.objects.all()
    authors = Author.objects.all()


    latest_three = Blog.objects.all().order_by('-id')[:3]

    # print(request.user)

    context = {
        'blogs': blogs, 
        'categories':categories,
        'authors':authors,
        'latest_three':latest_three,
    }
    
    return render(request, 'index.html', context)

@login_required(login_url='/login')
def all_blogs(request):
    return render(request, 'blogs.html')

@login_required(login_url='/login')
def single_blog(request, id):
    blog = Blog.objects.get(id=id)

    categories = Category.objects.all()

    comments=Comment.objects.filter(blog_id=id)
    count=len(comments)

    context = {
        'blog': blog, 
        'categories':categories,
        'comments' : comments,
        'count' : count
    }

    return render(request, 'blog.html', context)

def signup(request):
    # if method -> POST 
    if request.method == 'POST':
        # Values fetch 
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        pswd1 = request.POST['pswd1']
        pswd2 = request.POST['pswd2']

        # Pass word match
        if pswd1 == pswd2:
            if User.objects.filter(username=username).exists():
                # Pass a message that username already exists
                messages.error(request, "Username already exists")
                return redirect("/signup")
            
            if User.objects.filter(email=email).exists():
                # Pass a message that email is already in use
                messages.error(request, "Email is already in use")
                return redirect("/signup")
            
            # Create a new user 
            User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=pswd1)
            # Pass a message that signup successful. Please login now
            messages.success(request, "Account created successfully. Please login to access further")
            return redirect("/login")

        else: 
            messages.error(request, "Passwords do not match")
            return redirect("/signup")
        
    return render(request, 'signup.html')

def login(request):
    # if request -> POST:
    if request.method == 'POST':
        # values fetch 
        username = request.POST['uname']
        pswd = request.POST['pswd']

        # Authenticate 
        user = auth.authenticate(request, username=username, password=pswd)

            # If user found:
        if user is not None:
            # Login -> Redirect to home page
            auth.login(request, user)   # Start a Cookie-based session for the user 
            messages.success(request, "Login successful")
            return redirect("/")
        else:
            # Message: Invalid credentials
            messages.error(request, "Invalid credentials. Please try again")
            # redirect back to login 
            return redirect("/login")

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, "Logout successful")
    return redirect("/login")

def register_author(request):
    user = request.user
    if request.method =="POST":
        # fetch form data
        age = request.POST['age']
        phone = request.POST['phone']
        image = request.FILES['image']

        # fetch name, email from database
        name = user.first_name + user.last_name
        email = request.user.email

        # create author object
        # save the object

        Author.objects.create(name=name, age=age, phone=phone, email=email, image=image, user=user)

        return redirect("/")
    return render(request, 'register_author.html')


def user_dashboard(request):
    # Fetch the author
    author = request.user.author
    if request.method=="GET":
        sortby='date'
    elif request.method=="POST":
        sortby=request.POST['sortby']
    # Filter the blogs by authors
    if sortby=='date':
        blogs = Blog.objects.filter(author=author)
        blogs=blogs[::-1]

    elif sortby=='length':
        blogs = Blog.objects.filter(author=author).order_by(Length('description'))

    n_comments=[]

    for blog in blogs:
        comments=Comment.objects.filter(blog_id=blog.id)
        n_comments.append(len(comments))

    blog_comment_pairs =zip(blogs, n_comments)
    context = {
        'blog_comment_pairs' : blog_comment_pairs,
    }

    return render(request, 'user_dashboard.html', context)

def add_blog(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category = request.POST['category']
        image = request.FILES['image']
        author = request.user.author
        category_obj = Category.objects.get(name=category)

        Blog.objects.create(title=title, description=description, category=category_obj, author=author, image=image)

        return redirect("/dashboard")
    context = {
        'categories':categories,
    }
    return render(request, 'add_blog.html', context)

def category_wise(request, name):
    cat = Category.objects.get(name=name)
    blogs = Blog.objects.filter(category=cat)

    context = {
        'category': name, 
        'blogs': blogs,
    }
    return render(request, 'category_blogs.html', context)

def delete_blog(request, id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    return redirect("/dashboard")

def add_comment(request, id):
    if request.method=='POST':
        blog_obj=Blog.objects.get(id=id)
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        author = request.user.author

        
        Comment.objects.create(blog=blog_obj, name=name, email=email, subject=subject, message=message, author=author)
    
        return redirect(f'/blog/{id}')
    
    


