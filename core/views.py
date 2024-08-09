from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from notes.models import Note
from documents.models import Document
from kalendar.models import CalendarEvent


@login_required
def home(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    notes = Note.objects.filter(user=user)
    documents = Document.objects.filter(user=user)
    events = CalendarEvent.objects.filter(user=user)

    context = {
        'tasks': tasks,
        'notes': notes,
        'documents': documents,
        'events': events,
    }
    return render(request, 'core/home.html', context)
