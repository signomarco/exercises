from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

       
class Ticket(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Support Ticket"
        verbose_name_plural = "Support Tickets"
        
try:
    int(input("Press Enter to continue..."))

except KeyboardInterrupt:
    print("You have cancelled the operation.")

except Exception as e:
    print(str(e))