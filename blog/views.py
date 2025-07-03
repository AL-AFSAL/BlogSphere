from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post , AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm 
# Create your views here.
#posts = [
#        {'id':1,'title': 'Post 1','Content': 'Content of Post 1','Sport': 'Tennis'},
#        {'id':2,'title': 'Post 2','Content': 'Content of Post 2','Sport': 'Soccer'},
#        {'id':3,'title': 'Post 3','Content': 'Content of Post 3','Sport': 'baseket ball'},
#        {'id':4,'title': 'Post 4','Content': 'Content of Post 4','Sport': 'base ball'},
#        {'id':5,'title': 'Post 5','Content': 'Content of Post 5','Sport': 'runing'},
#        {'id':6,'title': 'Post 6','Content': 'Content of Post 6','Sport': 'golf'},
#    ]

def index(request):
    blog_name = "WELCOME TO BLOG SITE"
    # getting data in base post models
    all_posts = Post.objects.all()
      
     #paginator
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
     

    return render(request, 'blog/index.html',{"blog_name":blog_name ,'page_obj':page_obj})


def post(request,slug):
    # getting static data 
    # post = next((item for item in post if item['id'] == int(post_id)), None)
    try:
        #getting data from model id 
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    
    
    except Post.DoesNotExist:
        raise Http404("This Page is Not Founded")

    #logger = logging.getLogger("TESTING")
    #logger.debug(f'post  varible is {post}')=
    return render(request, 'blog/detail.html', {'post': post , 'related_posts': related_posts })
    
def old_url_redirect(request):
   return redirect(reverse('blog:new_url_view'))

def new_url_view(request):
    return HttpResponse(" WELCOME        OUR'S        NEW         URL         PAGE ")

def contact_views(request):
    if request.method == 'POST':
       form = ContactForm(request.POST)
       name = request.POST.get('name')
       email = request.POST.get('email')
       message = request.POST.get('message')
       #form.cleaned_data['name']
       logger = logging.getLogger("TESTING")
       if form.is_valid():
          logger.debug(f'POST Data is == {form.cleaned_data['name'] } {form.cleaned_data['email']} {form.cleaned_data['message']}' )
          successs_message = 'Your Email Has Been Sent!!!!! '
          return render(request, 'blog/contact.html',{'form':form , 'successs_message':successs_message})
       else:
           logger.debug('SORRY YOU ENTER THE FEILD!!!!!!!!')
           return render(request, 'blog/contact.html',{'form':form , 'name':name , 'email':email , 'message':message})
    return render(request, 'blog/contact.html')

def aboutus_views(request):
    about_instance = AboutUs.objects.first()
    about_content = about_instance.content if about_instance else "Welcome to BlogSphere! Content coming soon..."
    return render(request, 'blog/aboutus.html', {'about_content': about_content})



