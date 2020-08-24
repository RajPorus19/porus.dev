from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
        
    form = ContactForm()
    context = {'form':form, 'message':''}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            context = {
                'form':form,
                 'message':'Your message has been sent with success'
                 }
    return render(request, 'contact/contact.html', context)