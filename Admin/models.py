from django.db import models

# Create your models here.

class QuesType(models.Model):
     typename = models.CharField(max_length=50)

     def __str__(self):
         return self.typename

class Query_table(models.Model):
    quesion = models.CharField(max_length=400)
    answer = models.TextField()
    satisfied=models.IntegerField("satisfied",default=0)
    unsatisfied=models.IntegerField("unsat",default=0)
    viewed=models.IntegerField("viewed",default=0)
    queType = models.ForeignKey(QuesType,on_delete=models.CASCADE)

class list_unsat(models.Model):
    question = models.CharField(max_length=400)
    dbqid = models.IntegerField("dbqid",default=0)


