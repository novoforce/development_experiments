from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club

# Create your views here.
class ClubChartView(TemplateView):
    template_name= 'clubs/chart.html' #specific templates inside the template folder


    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["qs"] = Club.objects.all()
        return context


