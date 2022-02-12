from django.shortcuts import redirect, render
from .forms import Contact
from django.core.mail import EmailMessage


# Create your views here.


def contactview(request):
    if request.method=="POST":
        form=Contact(data=request.POST)
        if form.is_valid():
            nameform=request.POST.get('name')
            emailform=request.POST.get('email')
            subjectform=request.POST.get('subject')
            email=EmailMessage('Message from DjangoBlog', f'{nameform}\n{emailform}\n\n{subjectform}', '', ['aramaper28@gmail.com'], reply_to=(emailform,))
            try:
                email.send()
            except:
                return redirect('/contact/?novalid')
            else:
                return redirect('/contact/?valid')
    else:
        form=Contact()
    return render(request, 'contactapp/contact.html', {'form':form})
    
