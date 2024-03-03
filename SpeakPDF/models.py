from django.contrib.auth.models import User
from django.db import models

class AudioConvert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='audioFiles/')
    audio_file = models.FileField(upload_to='audio/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.file.name} - {self.audio_file.name} - {self.date}'

class LanguageConvert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='langFiles/')
    audio_file = models.FileField(upload_to='language/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.file.name} - {self.audio_file.name} - {self.date}'

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.user.username} - {self.title}'
