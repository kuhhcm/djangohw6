from .models import Todo

for record in Todo.objects.all():
    if int(record.id) % 2 != 0:
        record.delete()