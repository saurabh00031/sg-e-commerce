from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):      
    is_user = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)






INTEREST_CHOICES=(
('education','education'),
('health','health'),
('food','food'),
('electronics','electronics'),
('real_estate','real_estate'),
('softwares','softwares'),
('fashion','fashion'),
('footwears','footwears'),
('transport','transport'),
('ayurveda','ayurveda')
)



class Usrinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_Name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    git_hub=models.CharField(max_length=50)
    insta_link=models.CharField(max_length=50)
    linked_in=models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country=models.CharField(max_length=100)
    address = models.TextField()
    field_of_interest=models.CharField(choices=INTEREST_CHOICES,max_length=100)
    total_earnings_by=models.CharField(max_length=100)



class Mentorinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    full_Name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    git_hub=models.CharField(max_length=50)
    insta_link=models.CharField(max_length=50)
    linked_in=models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.TextField()
    states=models.TextField()
    country=models.CharField(max_length=100)
    field_of_interest=models.CharField(choices=INTEREST_CHOICES,max_length=100)
    total_earnings_by=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    experience_yrs=models.CharField(max_length=20)
    description_in_short=models.TextField()
    future_goals=models.TextField()

    def save(self, *args, **kwargs):
        super(Mentorinfo, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)




class government_Notificationsinfo(models.Model):
    notify_title=models.CharField(max_length=100)
    notify_body=models.CharField(max_length=200)
    notify_by_whom=models.CharField(max_length=200)
    notify_dates= models.DateTimeField()
    
class Blog_Post(models.Model):
    image = models.ImageField(upload_to = 'img')
    title = models.CharField(max_length= 200)
    body = models.TextField()
    slug = models.SlugField()
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    commenter = models.CharField(max_length = 50)
    body = models.TextField()
    post = models.ForeignKey(Blog_Post, on_delete = models.CASCADE, related_name='comments')
    def __str__(self):
        return self.body

        