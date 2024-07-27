from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Seminars,Profile,ContactUs,SharkTank,OldSharkTank,eventsUpcoming
from django.core.paginator import Paginator
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def NewHome(request):
    Semi = Seminars.objects.order_by('-date')
    # paginator=Paginator(Semi,2)
    # page_number=request.GET.get('page')
    # Seminars1=paginator.get_page(page_number)

    event1=SharkTank.objects.order_by('-maindate')
    # paginator1=Paginator(event1,2)
    # page_number1=request.GET.get('page')
    # eventss=paginator1.get_page(page_number1)

    event2=OldSharkTank.objects.order_by('-maindate')
    profile=Profile.objects.order_by('priority')
    newPara={'seminars': Semi,'events':event1,  'profile':profile,'OldEvent':event2}
    return render(request,"index.html",newPara)


def contact(request):
    create=False
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        m_number = request.POST.get('m_number')
        email_subject = request.POST.get('email_subject')
        message = request.POST.get('message')
        


        # Basic validation
        errors = []
        if not full_name:
            errors.append("Full Name is required.")
        if not email:
            errors.append("Email is required.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append("Email is not valid.")
        if not m_number:
            errors.append("Mobile Number is required.")
        if not email_subject:
            errors.append("Email Subject is required.")
        if not message:
            errors.append("Message is required.")

        if errors:
            # If there are validation errors, render the form again with errors
            return render(request, 'contact.html', {'errors': errors, 'full_name': full_name,
                                                    'email': email, 'm_number': m_number,
                                                    'email_subject': email_subject, 'message': message})
        else:
            create=True
        

        # If validation passes, save to the database
        contact_message = ContactUs.objects.create(
            full_name=full_name,
            email=email,
            mobile_number=m_number,
            email_subject=email_subject,
            message=message
        )
       
        contact_message1 = {'full_name':full_name,'created':create}
        cotent = {'content': contact_message1}
        return render(request,'contact.html',cotent)

    else:
        return render(request, 'contact.html')
        # Assuming success, redirect to a success page or show a success message
        # return render(request, '')
        
def eventsUp(request):
    events = eventsUpcoming.objects.order_by('-date')
    newPara = {'eventup':events}
    return render(request, 'eventsUpcoming.html',newPara)



def sharkTank(request):
    event1=SharkTank.objects.order_by('-maindate')
    # paginator1=Paginator(event1,2)
    # page_number1=request.GET.get('page')
    # eventss=paginator1.get_page(page_number1)

    event2=OldSharkTank.objects.order_by('-maindate')
    newPara={'events':event1,'OldEvent':event2}
    return render(request, 'sharkTank.html',newPara)
    