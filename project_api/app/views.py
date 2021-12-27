import csv

from django.http import HttpResponse, Http404

from .models import User, Task
from .api_data_scraper import api_get_user_data, api_get_task_data


def csv_output(request):
    user_data = api_get_user_data('users')
    task_data = api_get_task_data('todos')
    if user_data and task_data:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=users_tasks.csv'
        writer = csv.writer(response)
        writer.writerow(['User name', 'City', 'Task title', 'Task boolean'])
        for task in Task.objects.all().order_by('user_id'):
            user = User.objects.get(id=task.user_id)
            writer.writerow([user.full_name, user.address.city, task.title, task.completed])
        return response
    raise Http404('No response from api')
