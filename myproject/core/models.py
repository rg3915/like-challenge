from django.db import models

class Theme(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=100, unique=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(default=0)
    unlike = models.PositiveIntegerField(default=0)
    score = models.FloatField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.score = int(self.like) - int(self.unlike) / 2
        super(Video, self).save(*args, **kwargs)