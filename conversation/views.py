from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConversationMessageForm
from django.contrib.auth.models import User
from base.models import TourSite
from .models import Conversation, ConversationMessage




# def home(request):
#     return render(request, 'index.html')

def new_conversation(request, pk):
    tour = get_object_or_404(TourSite, pk=pk)

    if tour.created_by == request.user:
        return redirect('about')
    
    conversations = Conversation.objects.filter(tour=tour).filter(members__in=[request.user.id])

    # if conversations:
    #     return redirect('detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(tour=tour)
            conversation.members.add(request.user)
            conversation.members.add(tour.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('about')
    else:
        form = ConversationMessageForm()

    context = {
        'form':form,
        'conversations':conversations
    }
    return render(request, 'new.html',context)


def about(request):
    tours = TourSite.objects.all()

    context = {
        'tours':tours
    }

    return render(request,'question.html', context)

def detail(request):
    return render(request,'detail.html')

