from django.db import models
from django.conf import settings
# Create your models here.


class ButtonTable(models.Model):
    is_active = models.BooleanField(default=True)

    def change_status(self):
        self.is_active = not self.is_active

        self.save()


class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FilePathField(allow_folders=settings.MEDIA_ROOT)

    @staticmethod
    def create(file_path):
        file = File.objects.create(file=file_path)

        file.save()

        return file