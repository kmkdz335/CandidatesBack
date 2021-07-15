from django.db import models

# Create your models here.

class Candidates(models.Model):
    id_candidates = models.AutoField(primary_key = True)
    f_i_o = models.CharField(max_length=255, null=False)
    birth_date = models.DateField(null=False)
    add_date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255, null=False)
    review = models.CharField(max_length=255, null=False)
    working_place = models.CharField(max_length=255, null=False)
    salary = models.CharField(max_length=255, null=False)
    position = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.f_i_o

class Technologies(models.Model):
    id_tech = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Link(models.Model):
    id_link = models.AutoField(primary_key=True)
    id_candidates = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    id_tech = models.ForeignKey(Technologies, on_delete=models.CASCADE)
    level = models.CharField(max_length=255, null=False)

    def __str__(self):
        return str(self.id_link)