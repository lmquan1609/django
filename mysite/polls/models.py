from django.db import models

# After completing db model, auto create db: "python manage.py makemigrations", and then "python manage.py migrate"
# To test:
# python manage.py shell
# from polls.models import Question
# Question.objects.all()
# from django.utils import timezone
# q = Question(question_text='Which color do you like?', time_pub=timezone.now())
# q.save()
# q.id
# q.question_text
# c = Choice(question=q, choice_text='red', vote=0)
# c.save()
# d = Choice(question=q, choice_text='green', vote=0)
# d.save()

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)