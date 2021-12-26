import requests

from .models import User, Address, Task


def get_data_from_url(value=None):
    if value in ['users', 'todos']:
        r = requests.get(f'https://jsonplaceholder.typicode.com/{value}')
        if r.status_code == 200:
            return r.json()


def api_get_user_data(data=False):
    user_response = get_data_from_url(data)
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
            Address.objects.update_or_create(
                user=obj_user, defaults={
                    'street': addr_items.get('street'),
                    'suite': addr_items.get('suite'),
                    'city': addr_items.get('city'),
                    'zipcode': addr_items.get('zipcode')
                }
            )
        return True


def api_get_task_data(data=False):
    task_response = get_data_from_url(data)
    if task_response:
        for item in task_response:
            Task.objects.update_or_create(
                user_id=item.get('userId'), id=item.get('id'), defaults={
                    'id': item.get('id'),
                    'title': item.get('title'),
                    'completed': item.get('completed')
                }
            )
        return True
