from django.db.models.signals import post_save
from .models import Stream, Post




# Signal to auto-create stream records when post is created
post_save.connect(Stream.add_post, sender=Post)