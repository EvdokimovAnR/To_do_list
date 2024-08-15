from django.db import models
from users.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField("Название задания", max_length=512, null=True, blank=True)
    is_completed = models.BooleanField("Завершено", default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
        ordering = ['is_completed']

    def str(self):
        return self.title