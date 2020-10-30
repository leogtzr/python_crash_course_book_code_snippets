from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # owner field to Topic, which establishes a foreign key relationship to the
    # User model. If a user is deleted, all
    # the topics associated with that user will be deleted as well.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    # on_delete=models.CASCADE argument tells Django that
    # when a topic is deleted, all the entries associated
    # with that topic should be deleted as well.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    # Meta information I guess ...
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ Return a string representation of the model."""
        return f"{self.text[:50]}..."
