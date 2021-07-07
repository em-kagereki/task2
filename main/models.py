from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name=models.CharField
    
    def __str__(self):
        return self.name
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField
    complete =models.BooleanField()
    
    def __str__(self):
        return self.text
    
    