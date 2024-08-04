from django.db import models

# Create your models here.from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    hours = models.PositiveIntegerField()
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    package_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.regular_Price} OMR"

class DiscountCode(models.Model):
    code = models.CharField(max_length=50)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

class CourseRegistration(models.Model):
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
    ]
    CATEGORY_CHOICES = [
        ('freelancer', 'Freelancer'),
        ('employee', 'Employee'),
        ('job_seeker', 'Job Seeker'),
        ('student', 'University/College Student'),
        ('passionate', 'Passionate'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    civil_id = models.CharField(max_length=50)
    discount_code = models.ForeignKey(DiscountCode, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    
class Sublevels(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    level_name = models.CharField(max_length=100)
    level_price = models.DecimalField(max_digits=10, decimal_places=2)


