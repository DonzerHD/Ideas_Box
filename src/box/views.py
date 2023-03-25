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
    """
    View to create a new Ideas_Box instance
    """
    if request.method == 'POST':
        form = IdeasBoxForm(request.POST)
        if form.is_valid():
            # Get the title and description data from the form
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')

            # Create a new Ideas_Box object and save it to the database
            new_ideas_box = Ideas_Box(title=title, description=description, createur=request.user)
            new_ideas_box.save()
            return redirect('index')
    else:
        form = IdeasBoxForm()

    return render(request, 'box/create_box.html', {'form': form})

@login_required
def lists_box(request):
    """
    View to display the list of Ideas_Boxes
    """
    # Get the sorting criteria from the GET request or set default to 'date'
    order_by = request.GET.get('order_by', 'date')

    # Retrieve the Ideas_Boxes and order them according to the sorting criteria
    if order_by == 'votes':
        box_list = Ideas_Box.objects.annotate(total_votes=F('upvotes') + F('downvotes')).order_by('-total_votes', '-date')
    else:
        box_list = Ideas_Box.objects.order_by('-date')

    # Get the list of Ideas_Box IDs voted by the current user
    user_votes = Vote.objects.filter(user=request.user).values_list('box', flat=True)

    # Apply pagination to the list of Ideas_Boxes
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
    # Get the ideas box object or 404 page
    box = get_object_or_404(Ideas_Box, id=box_id)

    try:
        # Save the vote object for the user and the ideas box
        vote = Vote(user=request.user, box=box, vote_type=vote_type)
        vote.save()

        # Increase the upvote or downvote count based on the vote_type and save the ideas box object
        if vote_type == 'upvote':
            box.upvotes += 1
        elif vote_type == 'downvote':
            box.downvotes += 1
        box.save()
    except IntegrityError:
        # If a user has already voted on the same ideas box, do nothing
        pass

    # Redirect the user to the list_box page
    return redirect('list_box')
