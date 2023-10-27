from django.db import models


class TvShow(models.Model):
    CHOICE_ACT = (
        ('ДА', "ДА"),
        ('НЕТ', "НЕТ")
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='film/', null=True)
    act = models.CharField(max_length=100, choices=CHOICE_ACT)
    cost = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title