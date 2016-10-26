from django.shortcuts import render,get_object_or_404,redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
#comment
from comments.models import Comments
from comments.forms import CommentForm
from django.contrib.contenttypes.models import ContentType


# Create your views here.



def home(request):
	return render(request,"home.html",{})

@login_required(login_url='/login/')
def post(request):
	title = "Create Post"
	form  = PostForm(request.POST or None , request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.user = request.user
		instance.save()
		return redirect('retrive')
	context = {
	"form"  : form,
	"title"  : title,
 	}
	return render(request,"post.html",context)

def retrive(request):
	queryset_list = Post.objects.all()

	srch = request.GET.get("q")
	if srch:
	 	queryset_list  = queryset_list.filter(title__icontains=srch)

	paginator = Paginator(queryset_list, 10) 

	page = request.GET.get('page')
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)

	#query = Post.objects.all()#.order_by("-timestamp" , "-update")
	context = {
	"query" : queryset,
	#"query_list" :queryset,
	}
	return render(request , "retrive.html" , context)


def details(request,id = None):
	instance 	= get_object_or_404(Post,id=id)


	initial_data = {
		"content_type" : instance.get_content_type,
		"object_id" : instance.id,
	}
	form = CommentForm(request.POST or None, initial = initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		obj_id = form.cleaned_data.get("object_id")
		content_data = form.cleaned_data.get("content")
		content_type = ContentType.objects.get(model = c_type)

		new_comment , created = Comments.objects.get_or_create(
										user  =request.user,
										content_type = content_type,
										object_id = obj_id,
										content = content_data,
										
			)
		return HttpResponseRedirect(instance.get_absolute_url())
	comments = instance.comments
	context = {
	'instance' : instance,
	'comment_form' : form,
	'comments' : comments,
	}

	return render(request,'details.html', context)
def update(request,id=None):
	title = "Update Post"
	instance = get_object_or_404(Post ,id=id)
	form  = PostForm(request.POST or None , request.FILES or None,instance = instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.user = request.user
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form"  : form,
	"title"  : title,
 	}
	return render(request,"post.html",context)
def delete_post(request,id=None):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	return redirect("retrive")
	

