from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime

from .models import Todo, CompletedTodo

# Create your tests here.

def create_todo(todo_title, priority, text, days):
    time = timezone.now() +  datetime.timedelta(days =days)
    return Todo.objects.create(todo_title = todo_title, priority=priority,
    text= text, due_date = time)

def create_completedTodo(todo_title, priority, text, days):
    time = timezone.now() +  datetime.timedelta(days =days)
    return CompletedTodo.objects.create(todo_title = todo_title, priority=priority,
    text= text, due_date = time)

class IndexViewTests(TestCase):
    def test_no_todos(self):
        #test for the case when there is no todo
        #checks status code, whether it includes certain text,
        #and queryset
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "현재로서 할일 없음")
        self.assertQuerysetEqual(response.context['todo_list'],
         [])

    def test_expired_todos(self):
        #test for the case when there is one expired todo
        #notification function has to be successful
        #checks status code, whether it includes certain text,
        #and queryset
        create_todo('expired', 5, 'expired', 0)
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "알림!")
        self.assertQuerysetEqual(response.context['expired_list'],
        ['<Todo: expired>'])

    def test_one_expired_and_one_notexpired_todo(self):
        #test for case when there is one expired,
        #and the other is not expired todo
        #checks status code, whether it includes certain text,
        #and queryset
        create_todo('expired', 5, 'expired', 0)
        create_todo('not expired', 5, 'not expired',1)
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "알림!")
        self.assertQuerysetEqual(response.context['expired_list'],
        ['<Todo: expired>'])
        self.assertQuerysetEqual(response.context['todo_list'],
        ['<Todo: expired>','<Todo: not expired>'])

class DetailViewTests(TestCase):
    def test_one_todo(self):
        #tests for ordinary case of detailview,
        #which is the case when detailview gets one todo object
        #checks whether it contains certain text
        todo = create_todo('one todo', 5, 'I like apple', 0)
        url = reverse('todo:detail', args=(todo.id,))
        response =self.client.get(url)
        self.assertContains(response, todo.text)

class completedListViewTests(TestCase):
    def test_no_completedTodo(self):
        #tests for case when where is no completedTodo
        #checks status code, whether it conatins certain text,
        #and queryset
        response = self.client.get(reverse('todo:completed'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "완료한 일이 하나도 없음..")
        self.assertQuerysetEqual(response.context['completed_list'], [])

    def test_one_completedTodo(self):
        #test for case when there is one completedTodo
        #check whether it contains certain text
        todo =create_completedTodo('completed',5,'I love apple',0)
        response = self.client.get(reverse('todo:completed'))
        self.assertContains(response, todo.todo_title)
