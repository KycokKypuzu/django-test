from django.db import models

from tasks.models import Project, Task


# Create your models here.


class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    BUG_PRIORITY = [
        ('1', 'Дедлайн 1 год'),
        ('2', 'Дедлайн 1 квартал'),
        ('3', 'Дедлайн 1 месяц'),
        ('4', 'Дедлайн 1 неделя'),
        ('5', 'Дедлайн 1 день'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(  # А это точно из tasks? А если я Project создам в quality_control?
        Project,
        related_name='bugs',  # надо ли это оставлять?
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.CharField(  # Следует ли сделать так или можно по-другому?
        max_length=50,
        choices=BUG_PRIORITY,
        default='1',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    STATUS_CHOICES = [  # Нормально ли обзывать разные вещи в разных классах одним и тем же именем?
        ('Review', 'На рассмотрении'),
        ('Accepted', 'Принято в обработку'),
        ('Declined', 'Отклонено'),
    ]
    REQUEST_PRIORITY = [
        ('1', 'Дедлайн 1 год'),
        ('2', 'Дедлайн 1 квартал'),
        ('3', 'Дедлайн 1 месяц'),
        ('4', 'Дедлайн 1 неделя'),
        ('5', 'Дедлайн 1 день'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='request',  # надо ли это оставлять?
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,  # это так делается или нет?
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.CharField(  # Следует ли сделать так или можно по-другому?
        max_length=50,
        choices=REQUEST_PRIORITY,
        default='1',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
