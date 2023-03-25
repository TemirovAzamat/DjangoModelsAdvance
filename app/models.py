from datetime import datetime
from django.db import models as m


class AbstractPerson(m.Model):
    name = m.CharField(max_length=30)
    birth_date = m.DateField()

    def get_age(self):
        return self.birth_date - datetime.now()

    class Meta:
        abstract = True


class Employee(AbstractPerson):
    position = m.CharField(max_length=20)
    salary = m.CharField(max_length=10)
    work_experience = m.IntegerField()

    def __str__(self):
        return f'Сотрудник: {self.name}, позиция: {self.position}'


class Passport(m.Model):
    inn = m.CharField(max_length=14)
    id_card = m.CharField(max_length=7)
    employee = m.OneToOneField(Employee, on_delete=m.CASCADE)

    def get_gender(self):
        if self.inn[0] == '2':
            return 'Пол: Мужчина'
        elif self.inn[0] == '1':
            return 'Пол: Женщина'

    def __str__(self):
        return f'ИНН: {self.inn}, ID: {self.id_card}'


class WorkProject(m.Model):
    project_name = m.CharField(max_length=20)
    members = m.ManyToManyField(Employee, related_name='works', through='Membership')

    def __str__(self):
        return self.project_name


class Membership(m.Model):
    member = m.ForeignKey(Employee, on_delete=m.CASCADE)
    works = m.ForeignKey(WorkProject, on_delete=m.CASCADE)
    date_joined = m.DateField()

    def __str__(self):
        return f'Сотрудник: {self.member}, проект: {self.works}, дата присоединения - {self.date_joined}'


class Client(AbstractPerson):
    address = m.CharField(max_length=20)
    phone_number = m.CharField(max_length=12)

    def __str__(self):
        return f'Клиент: {self.name}, адрес: {self.address}'


class VIPClient(Client):
    vip_status_start = m.DateField(default=datetime.now)
    donation_amount = m.IntegerField()

    def __str__(self):
        return f'ВИП клиент: {self.name}, дата старта: {self.vip_status_start}, пожертвовал: {self.donation_amount}'
