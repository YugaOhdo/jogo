from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    contacts = Contact.objects.all().order_by('-id')
    paginator = Paginator(contacts, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
    return render(
        request, 
        'contact/index.html',
        context,
        
    )
def oneContact(request, contact_id):
    # single_contact =  Contact.objects.filter(pk=contact_id).first()
    # # single_contact = Contact.objects.get(pk=contact_id)
    # if single_contact is None:
    #     raise Http404()
    single_contact = get_object_or_404( Contact.objects.filter(pk=contact_id), show=True)
        
    context = {
        'contact': single_contact
    }

    return render(
        request, 
        'contact/contact.html',
        context
    )
def search(request): 
    search_value = request.GET.get('q', '').strip()
    if search_value == '':
        return redirect('contact:index')
        
    contacts = Contact.objects.filter(show=True)\
    .filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) 
        # podemos fazer o mesmo para qualquer campo
        
    )\
    .order_by('-id')
    
    # print(contacts.query)
    paginator = Paginator(contacts, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'search_value': search_value,
    }
    
    return render(
        request, 
        'contact/index.html',
        context
     )
        