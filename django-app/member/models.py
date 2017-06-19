from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @property
    def find_set(self):
        result =[]
        for student in self.alls.all():
            result.append(student.name)

        return result




class Student(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey(
        Teacher,
        related_name='alls',
    )

    def __str__(self):
        return self.name

    #t1.find_set
    # t1 -> 학생이름 다불러오기