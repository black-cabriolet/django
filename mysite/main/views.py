from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")
    """
    Your index function in Django is designed to retrieve a ToDoList object based on its ID and then display its name in an HTTP response using Django's HttpResponse class
        View function to display the name of a ToDoList based on its ID.

    Args:
        response: The Django response object.
        id: The ID of the ToDoList to retrieve.

    Returns:
        An HTTP response containing the name of the ToDoList in an <h1> tag.

    """
    return render(response, "main/list.html", {'ls': ls})


def home(response):
    return render(response, "main/home.html", {"name":"Tyreek"})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
