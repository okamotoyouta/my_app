from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.views import generic
from .models import Update, UpdateDetail

class UpdateList(generic.ListView):
    model = Update
    template_name = "top/UpdateList.html"
    context_object_name = "updates"
    ordering = ["-date_posted"]


class UpdateDetailPage(generic.DetailView):

    model = Update

    template_name = "top/UpdateDetailPage.html"
    context_object_name = "update"
