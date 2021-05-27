from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name =models.CharField(max_length=200)

class Webpage(models.Model):
     topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
     name = models.CharField(max_length=264)
     url = models.URLField(unique=True)



class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()


# from django.db import models
#
#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
