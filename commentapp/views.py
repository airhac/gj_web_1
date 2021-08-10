from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class CommentCreationView(CreateView):
    model = Comment
