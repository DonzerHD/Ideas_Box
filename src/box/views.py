from django.db import IntegrityError
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F

from box.forms import IdeasBoxForm
from box.models import Ideas_Box, Vote

# Create your views here.
@login_required
def create_ideas_box(request):
    if request.method == 'POST':
        form = IdeasBoxForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')

        
            new_ideas_box = Ideas_Box(title=title, description=description, createur=request.user)
            new_ideas_box.save()
            return redirect('index')
    else:
        form = IdeasBoxForm()

    return render(request, 'box/create_box.html', {'form': form})

@login_required
def lists_box(request):
    order_by = request.GET.get('order_by', 'date')
    if order_by == 'votes':
        box_list = Ideas_Box.objects.annotate(total_votes=F('upvotes') + F('downvotes')).order_by('-total_votes', '-date')
    else:
        box_list = Ideas_Box.objects.order_by('-date')

    user_votes = Vote.objects.filter(user=request.user).values_list('box', flat=True)

    paginator = Paginator(box_list, 6)
    page = request.GET.get('page')

    try:
        boxs = paginator.page(page)
    except PageNotAnInteger:
        boxs = paginator.page(1)
    except EmptyPage:
        boxs = paginator.page(paginator.num_pages)

    return render(request, 'box/list_box.html', {'boxs': boxs, 'user_votes': user_votes, 'order_by': order_by})

@login_required
def vote(request, box_id, vote_type):
    box = get_object_or_404(Ideas_Box, id=box_id)

    try:
        vote = Vote(user=request.user, box=box, vote_type=vote_type)
        vote.save()

        if vote_type == 'upvote':
            box.upvotes += 1
        elif vote_type == 'downvote':
            box.downvotes += 1
        box.save()
    except IntegrityError:
        pass

    return redirect('list_box')
