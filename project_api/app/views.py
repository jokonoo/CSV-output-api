import csv
import requests

from django.http import HttpResponse

from .models import User, Address, Geo, Company, Task


def api_get_data():
    user_response = requests.get('https://jsonplaceholder.typicode.com/users')
    task_response = requests.get('https://jsonplaceholder.typicode.com/todos')

    for item in user_response.json():
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
        geo_items = addr_items.get('geo')
        obj_geo, created_geo = Geo.objects.update_or_create(
            address=obj_address, defaults={
                'lat': float(geo_items.get('lat')),
                'lng': float(geo_items.get('lng'))
            }
        )
        company_items = item.get('company')
        obj_company, created_company = Company.objects.update_or_create(
            user=obj_user, defaults={
                'name': company_items.get('name'),
                'catch_phrase': company_items.get('catchPhrase'),
                'bs': company_items.get('bs')
            }
        )
    for item in task_response.json():
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
