from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Todo(models.Model):
    title = models.CharField(_("عنوان"), max_length=100)
    descreption = models.CharField(_("توضیحات"), max_length=500)
    completed = models.BooleanField(_("وضعیت"), default=False)
    start_date = models.DateTimeField(_("زمان آغاز"), auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateTimeField(_("زمان پایان"), auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.title
