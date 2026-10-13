from django.db import models
from django.contrib.auth.models import AbstractUser
from diet_app.utility_func import calculate_bmr
# Create your models here.

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=15, unique=True)

class UserProfile(models.Model):
    age=models.PositiveIntegerField()
    
    weight=models.FloatField()
    height=models.PositiveBigIntegerField()
    gender_options=(
        ('male', 'male'),
        ('female', 'female')
    )
    gender=models.CharField(max_length=20, choices=gender_options)

    activity_options=(
        ("1.2", "no exercise"),
        ("1.375", "1-3 days/week"),
        ("1.55", "3-5 days/week"),
        ("1.725", "6-7 days/week"),
        ("1.9", "very intense activity")
    )
    activity_level=models.CharField(max_length=200, choices=activity_options)

    bmr=models.FloatField(null=True)

    owner=models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")


    def save(self, *args, **kwargs):
        self.bmr=calculate_bmr(self.age, self.weight, self.height, self.gender, self.activity_level)
        return super().save(*args, **kwargs)

class FoodLog(models.Model):
    name=models.CharField(max_length=200, null=True)

    MEAL_TYPE_OPTIONS=(
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack')
    )
    meal_type=models.CharField(max_length=100, choices=MEAL_TYPE_OPTIONS, null=True)
    calories=models.PositiveIntegerField(null=True)
    serving_size=models.CharField(max_length=100, null=True)
    notes=models.TextField(null=True)
    picture=models.ImageField(upload_to="foodlogs", null=True)
    owner=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="foodentries")

