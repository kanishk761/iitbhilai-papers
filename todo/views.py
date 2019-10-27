from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todoItem

def todoView(request):
    all_todo_items = todoItem.objects.all()
    return render(request, 'todo.html',
                  {'all_items': all_todo_items})
def addTodo(request):
    c = request.POST['content']
    new_item = todoItem(content = c)
    new_item.save()
    return HttpResponseRedirect('/todo/')
def deleteTodo(request, item_id):
    item_del = todoItem.objects.get(id=item_id)
    item_del.delete()
    return HttpResponseRedirect('/todo/')
