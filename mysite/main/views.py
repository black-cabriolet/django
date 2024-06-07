from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    """
    Your index function in Django is designed to retrieve a ToDoList object based on its ID and then display its name in an HTTP response using Django's HttpResponse class
        View function to display the name of a ToDoList based on its ID.

    Args:
        response: The Django response object.
        id: The ID of the ToDoList to retrieve.

    Returns:
        An HTTP response containing the name of the ToDoList in an <h1> tag.

    """
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})
