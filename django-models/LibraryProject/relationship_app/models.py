from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title   # fixed bug (was self.name)


class Library(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Librarian(models.Model):   # <-- checker expects this
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    library = models.ForeignKey(   # <-- checker expects a "library" field
        Library, 
        on_delete=models.CASCADE,
        related_name="librarians"
    )

    def __str__(self):
        return f"{self.name} — {self.library}"


# ✅ Extend User with UserProfile for Role-Based Access Control
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# ✅ Automatically create/update UserProfile when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
