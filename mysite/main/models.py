from django.db import models

# Create your models here.


class ToDoList(models.Model):
    """
    The ToDoList model represents a to-do list with a name attribute.

    Attributes:
        name (CharField): A string field with a maximum length of 200 characters representing the name of the to-do list.
    """

    name = models.CharField(max_length=200)

    def __str__(self):
        """
        Returns a string representation of the ToDoList instance.

        Returns:
            str: The name of the to-do list.
        """
        return self.name


class Item(models.Model):
    """
    The Item model represents an item within a to-do list.

    Attributes:
        todolist (ForeignKey): A foreign key linking the item to a specific ToDoList. If the ToDoList is deleted, the item will also be deleted (on_delete=models.CASCADE).
        text (CharField): A string field with a maximum length of 300 characters representing the text of the item.
        complete (BooleanField): A boolean field indicating whether the item is complete or not.
    """

    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        """
        Returns a string representation of the Item instance.

        Returns:
            str: The text of the item.
        """
        return self.text


"""
# Import necessary models
from main.models import Item, ToDoList

# Create a new ToDoList instance named "Tim's List"
t = ToDoList(name="Tim's List")
# Save the instance to the database
t.save()

# Retrieve all ToDoList instances
all_todo_lists = ToDoList.objects.all()
print(all_todo_lists)  # Output: <QuerySet [<ToDoList: Tim's List>]>

# Retrieve a specific ToDoList instance by its ID
tim_list = ToDoList.objects.get(id=1)
print(tim_list)  # Output: <ToDoList: Tim's List>

# Create another ToDoList instance named "Tyreek Kiritu Kinyanjui"
s = ToDoList(name="Tyreek Kiritu Kinyanjui")
# Save the instance to the database
s.save()

# Query all items related to 't' ToDoList
items_in_tim_list = t.item_set.all()
print(items_in_tim_list)  # Output: <QuerySet []>

# Create a new Item related to 't' ToDoList
new_item_in_tim_list = t.item_set.create(text="I am destined for greatness", complete=False)
print(new_item_in_tim_list)  # Output: <Item: I am destined for greatness>

# Query all items related to 't' ToDoList again
items_in_tim_list = t.item_set.all()
print(items_in_tim_list)  # Output: <QuerySet [<Item: I am destined for greatness>]>

# Create a new Item related to 's' ToDoList
new_item_in_ty_list = s.item_set.create(text="I AM SPEED", complete=False)
print(new_item_in_ty_list)  # Output: <Item: I AM SPEED>


##to delete
1 first you have to get the object to be deleted
del_object = get(id=1)
del_object.delete()
"""
