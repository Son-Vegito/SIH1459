from django.db import models


# Create your models here.
class State(models.Model):
    name = models.CharField('State Name',max_length=50)
    code = models.CharField('State Code', primary_key=True, max_length=2)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField('College Name', max_length=100)
    code = models.CharField('College Code', primary_key=True, max_length=5)
    state = models.ForeignKey(State, blank=False, null=False, on_delete=models.CASCADE)
    city = models.CharField('College City',max_length=100)
    pincode = models.CharField('College Pincode', max_length=6)
    address = models.CharField('College Address',max_length=200)
    phone = models.CharField('College Phone',max_length=10)
    created_at = models.DateTimeField('College Creation Date', auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField('Course Name',max_length=100)
    code = models.CharField('Course Code', primary_key=True, max_length=2)
    duration = models.IntegerField('Course Duration')
    created_at = models.DateTimeField('Course Creation Date', auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Scheme(models.Model):
    name = models.CharField('Scheme Name', null=False, blank=False,max_length=100)
    id = models.DecimalField('Scheme Id', primary_key=True, max_length=2, max_digits=2, decimal_places=0)
    created_at = models.DateTimeField('Scheme Creation Date', auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField('First Name',max_length=100)
    last_name = models.CharField('Last Name',max_length=100)
    uid = models.CharField('UID', primary_key=True, max_length=14)
    admission_year = models.IntegerField('Admission Year')
    date_of_birth = models.DateField('Date of Birth', null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Student Creation Date', auto_now_add=True)
    aadhar_id = models.CharField('Aadhar ID', max_length=12)
    scheme = models.ForeignKey(Scheme, on_delete=models.SET_NULL, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['aadhar_id']),
            models.Index(fields=['first_name', 'last_name']),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
