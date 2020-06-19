from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.views import generic
from .models import Topics




class TopicListView(generic.ListView):
    model = Topics
    template_name = "top/GrandeVueTop.html"
    ordering = ["-date_topiced"]
    context_object_name = "topics"
