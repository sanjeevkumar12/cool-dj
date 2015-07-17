from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from .models import TodoItem
class TodoList(ListView):
    model = TodoItem
    def get_template_names(self):
        return "todo/index.html"
    def get_queryset(self):
        try:
            return TodoItem.objects.select_related('todolist').filter(todolist__user=self.request.user)
        except TodoItem.DoesNotExist:
            return None
class ToDoItemDetailView(DetailView):
    model = TodoItem

    def get_object(self, queryset=None):
        print(self.kwargs)
        return TodoItem.objects.select_related('todolist').filter(todolist__user=self.request.user,todolist__slug = self.kwargs.get('todolistslug'),slug=self.kwargs.get('slug'))

class TodoEditView(FormView):
    template_name = 'todo/edittodo.html'

class TodoItemCreateView(FormView):
    template_name = "todo/create.html"

    def get_context_data(self, **kwargs):
        context = super(TodoItemCreateView,self).get_context_data(**kwargs)
        #context['todolists'] = To