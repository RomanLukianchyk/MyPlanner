from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from kalendar.models import CalendarEvent
from kalendar.forms import CalendarEventForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class CalendarEventListView(ListView):
    model = CalendarEvent
    template_name = 'calendar/calendar_event_list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        return CalendarEvent.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class CalendarEventDetailView(DetailView):
    model = CalendarEvent
    template_name = 'calendar/calendar_event_detail.html'
    context_object_name = 'event'


@login_required
def event_create(request):
    if request.method == 'POST':
        form = CalendarEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('calendar_view')
    else:
        form = CalendarEventForm()
    return render(request, 'calendar/calendar_event_form.html', {'form': form})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(CalendarEvent, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CalendarEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = CalendarEventForm(instance=event)
    return render(request, 'calendar/calendar_event_form.html', {'form': form})


@login_required
def event_delete(request, pk):
    event = get_object_or_404(CalendarEvent, pk=pk, user=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('calendar_view')
    return render(request, 'calendar/calendar_event_confirm_delete.html', {'event': event})
