from django.shortcuts import render, redirect
from blog_app.models import Author, Blog 

# Create your views here.
def home(request):
    return render(request, 'temp_admin/index.html')

def authors(request):
    # Show employees data
    authors = Author.objects.all()

    context = {
        'authors': authors
    }
    
    return render(request, 'temp_admin/docs.html', context)

def blogs(request):
    visible_blogs = Blog.objects.filter(hidden=False)
    v_count = visible_blogs.count()
    hidden_blogs = Blog.objects.filter(hidden=True)
    h_count = hidden_blogs.count()

    context = {
        'visible': visible_blogs,
        'hidden': hidden_blogs,
        'v_count': v_count,
        'h_count': h_count,
    }

    return render(request, 'temp_admin/orders.html', context)

def hide_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.hidden = True 

    blog.save() 

    return redirect("/superadmin/blogs")

def unhide_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.hidden = False 

    blog.save() 

    return redirect("/superadmin/blogs")

def results(request):
    if request.method == "POST":
        query = request.POST['search']
        in_title = Blog.objects.filter(title__contains=query)
        in_description = Blog.objects.filter(description__contains=query)

        results = list(in_title) + list(in_description)

        print(results)

        context = {
            'results': results,
        }

        return render(request, 'temp_admin/searchresults.html', context)