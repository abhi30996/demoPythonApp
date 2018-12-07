from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def as_json(self):
        return dict(
            question_text=self.question_text,
            pub_date=self.pub_date
        )


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def as_json(self):
        return dict(
            id = self.id,
            choice_text=self.choice_text,
            votes=self.votes
        )
