from django.db import models



# Program
class Program(models.Model):
    title = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
 
    def __str__(self):
        return self.title + self.branch
# Student
class Student(models.Model):
    roll_number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    dob = models.DateField('date of birth')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    # __str__ function   
    def __str__(self):
        d = self.program
        return self.roll_number + self.name  + d.title + d. branch

class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default='anonymous')
    email = models.EmailField(blank = True)
    describe = models.TextField(default = 'DataFlair Django tutorials')
    def __str__(self):
        return self.name