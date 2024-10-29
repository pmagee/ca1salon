from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import HairDresser, HairSalon, Client
from django.shortcuts import render

# Create your views here.
class ClientListView(ListView):
    model = Client
    template_name = 'clist.html'
    context_object_name = 'all_c_list'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'c_detail.html'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'c_create.html'
    fields = ['name', 'date_of_birth', 'salon']

class HairdresserUpdateView(UpdateView):
    model = HairDresser
    template_name = 'hd_edit.html'
    fields = ['salon']

class HairdresserDetailView(DetailView):
    model = HairDresser
    template_name = 'hd_detail.html'

class ChsListView(ListView):
    model = Client
    template_name = 'chs_list.html'
    context_object_name = 'all_c_list'

def query1(request):
    # Initialize an empty context to pass to the template
    context = {
        'client_name': None,
        'error_message': None,
    }

    try:
        oldest_client = Client.objects.earliest('date_of_birth')
        context['client_name'] = oldest_client.name
    except Client.DoesNotExist:
        context['error_message'] = "No clients found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query1.html', context)

def query2(request):
    # Initialize an empty context to pass to the template
    context = {
        'client_count': None,
        'error_message': None,
    }

    try:
        hair_salon = HairSalon.objects.get(name="Glamour Studio")
        client_count = Client.objects.filter(salon=hair_salon).count()

        context['client_count'] = client_count

    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    return render(request, 'db_query2.html', context)



