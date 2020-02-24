from django.db import models


class Message(models.Model):

    email = models.EmailField()
    message = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'messages'
        ordering = ('create_date',)
