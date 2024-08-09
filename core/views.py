from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import FastNote
from core.forms import FastNoteForm
from tasks.models import Task
from notes.models import Note
from documents.models import Document
from kalendar.models import CalendarEvent


@login_required
def home(request):
    user = request.user

    fast_note, created = FastNote.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = FastNoteForm(request.POST, instance=fast_note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FastNoteForm(instance=fast_note)

    tasks = Task.objects.filter(user=user)
    notes = Note.objects.filter(user=user)
    documents = Document.objects.filter(user=user)
    events = CalendarEvent.objects.filter(user=user)

    context = {
        'tasks': tasks,
        'notes': notes,
        'documents': documents,
        'events': events,
        'form': form,
    }
    return render(request, 'core/home.html', context)


@login_required
def save_fast_note(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        fast_note, created = FastNote.objects.get_or_create(user=request.user)
        fast_note.content = content
        fast_note.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)

