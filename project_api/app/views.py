import csv
import requests

from django.http import HttpResponse

from .models import User, Address, Task


def get_data_from_url(value=None):
    if value in ['users', 'todos']:
        return requests.get(f'https://jsonplaceholder.typicode.com/{value}').json()
    return None


def api_get_data():
    user_response = get_data_from_url('users')
    if user_response:
        for item in user_response:
            obj_user, created_user = User.objects.update_or_create(
                id=int(item.get('id')), defaults={
                    'full_name': item.get('name'),
                    'username': item.get('username'),
                    'email': item.get('email'),
                    'phone_number': item.get('phone'),
                    'website': item.get('website')
                }
            )
            addr_items = item.get('address')
            obj_address, created_address = Address.objects.update_or_create(
                user=obj_user, defaults={
                    'street': addr_items.get('street'),
                    'suite': addr_items.get('suite'),
                    'city': addr_items.get('city'),
                    'zipcode': addr_items.get('zipcode')
                }
            )
    task_response = get_data_from_url('todos')
    if task_response:
        for item in task_response:
            task_obj, task_created = Task.objects.update_or_create(
                user_id=item.get('userId'), id=item.get('id'), defaults={
                    'id': item.get('id'),
                    'title': item.get('title'),
                    'completed': item.get('completed')
                }
            )


def csv_output(request):
    api_get_data()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=users_tasks.csv'
    writer = csv.writer(response)
    writer.writerow(['User name', 'City', 'Task title', 'Task boolean'])
    for task in Task.objects.all().order_by('user_id'):
        user = User.objects.get(id=task.user_id)
        writer.writerow([user.full_name, user.address.city, task.title, task.completed])
    return response
