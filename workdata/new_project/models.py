from django.db import models


class SharkTank(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.TextField()
    maindate=models.DateField()
    title = models.TextField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return f"{self.title}"
    


class Seminars(models.Model):
    id=models.AutoField(primary_key=True)
    date = models.DateField()
    title = models.TextField()
    img = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

class Profile(models.Model):
    id=models.AutoField(primary_key=True)
    priority = models.IntegerField()
    name=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    gitlink=models.URLField()
    lnlink=models.URLField()
    iglink=models.URLField()

    def __str__(self):
        return f"{self.post}"

class ContactUs(models.Model):
    id=models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile_number=models.CharField(max_length=15)
    email_subject=models.CharField(max_length=150)
    message=models.TextField()

    def __str__(self):
        return f"{self.full_name}"



class OldSharkTank(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.TextField()
    maindate=models.DateField()
    title = models.TextField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return f"{self.title}"
    

class eventsUpcoming(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField()
    title = models.TextField()
    discription = models.TextField()
    img = models.ImageField(upload_to='pics')
    Formurl = models.URLField()

    def __str__(self):
        return f"{self.title}"

