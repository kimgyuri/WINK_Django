from django.db import models

class Myinfo(models.Model):
    name = models.CharField(max_length = 10)
    birth = models.DateField('Birthday')
    gender = models.CharField(max_length = 2)
    job = models.CharField(max_length = 10)
    tel = models.CharField(max_length = 15)
    mail = models.CharField(max_length = 25)
    nickname = models.CharField(max_length = 30)
    profile_img = models.ImageField(blank=True, null=True)
    self_intro = models.TextField()

class Board(models.Model):
    board_id = models.PositiveIntegerField(unique=True, default=1)
    name = models.CharField(max_length = 10)
    approved_board = models.BooleanField(default=False)

    def approve(self):
        self.approved_board = True
        self.save()
    
    def __str__(self):
        return self.text

    def number(self):
        num = Users.objects.count()
        if num == None:
            return 1
        else:
            return num + 1

class Post(models.Model):
    title = models.CharField(max_length = 20)
    date = models.DateField('Date')
    attatchfile = models.ImageField(blank=True, null=True)
    content = models.TextField()
    tag = models.CharField(max_length=20)
    delete = models.BooleanField(default=False)
    approved_post = models.BooleanField(default=False)
    content_like = models.PositiveIntegerField(unique=True, default=1)

    def approve(self):
        self.approved_post = True
        self.save()
    
    def __str__(self):
        return self.text
    
    def number(self):
        num = Users.objects.count()
        if num == None:
            return 1
        else:
            return num + 1

class Comment(models.Model):
    comment_id = models.PositiveIntegerField(unique=True, default=1)
    name = models.CharField(max_length = 10)
    date = models.DateField('Date')
    comment_like = models.AutoField(primary_key=True)
    delete = models.BooleanField(default=False)
    approved_comment = models.BooleanField(default=False)

    def number(self):
        num = Users.objects.count()
        if num == None:
            return 1
        else:
            return num + 1

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text


class GuestBook(models.Model):
    GuestBook_id = models.PositiveIntegerField(unique=True, default=1)
    name = models.CharField(max_length = 10)
    date = models.DateField('Date')
    img = models.ImageField(blank=True, null=True)
    content = models.TextField()
    approved_content = models.BooleanField(default=False)

    def number(self):
        num = Users.objects.count()
        if num == None:
            return 1
        else:
            return num + 1

    def approve(self):
        self.approved_content = True
        self.save()
    
    def __str__(self):
        return self.text
