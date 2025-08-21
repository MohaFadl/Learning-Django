from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    #A nice way to do TextChoices
    
    class Status(models.TextChoices):
        Draft = 'DF' , 'Draft',
        PUBLISHED = 'PB' , 'Published'
        
        
        
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   
    """
    another method we can use now from db instead of Python itself
    by adding 
    from django.db.models.functions import Now
    publish = models.DateTimeField(db_default=Now())
    """
    status = models.CharField(max_length=2,choices=Status , default=Status.Draft)

    """
    ordering => Configuring what will happen when we retrive the object from the database and how it will be represented
    indexes => Configuring what will happen when we retrive the object from the database and how it will be represented
    """
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, # what model do you want to connect to
        on_delete=models.CASCADE, # delete all posts if i delete the user
        related_name='blog_posts' # name of reverse releation user.blog_posts
        
    )
    
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
            ]


    def __str__(self):
        return self.title
    
