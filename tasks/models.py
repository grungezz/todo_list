from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['is_done', '-created_date']

    def __str__(self):
        return self.content
