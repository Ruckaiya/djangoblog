from django.shortcuts import render

from .models import NewPost, LatestPost, Popular


# Create your views here.
def post(request):
    newposts = NewPost.objects
    latestposts = LatestPost.objects
    populars = Popular.objects
    context = {
        'newposts': newposts,
        'latestposts': latestposts,
        'populars': populars
    }
    return render(request,'blogposts/blog.html', context)

