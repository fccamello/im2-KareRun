from django.shortcuts import get_object_or_404, redirect, render
from .forms import RegistrationForm
from RegLogCreate.models import Event


def event_reg(request, event_id):
    event = get_object_or_404(Event, eventid=event_id)
    eventname_split = event.eventname.split(' ', 1)
    first_word = eventname_split[0]
    rest_of_text = eventname_split[1] if len(eventname_split) > 1 else ''

    
    categories = event.eventcategory
    category_list = [f"{str(x)}km "for x in categories.split(',')]

    inclusions = event.inclusions
    inclusions_list = inclusions.split(',')


    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event  
            registration.save()
            return redirect('success') 
    else:
        form = RegistrationForm()

    return render(request, 'event_registration.html', {
        'event': event,
        'first_word': first_word,
        'form':form,
        'rest_of_text': rest_of_text,
        'categories': category_list,
        'inclusions': inclusions_list
    })
