from app.models import *

emp1 = Employee.objects.create(name='Азамат', birth_date='2004-10-18', position='Студент', salary='Доширак',
                               work_experience=5)
emp2 = Employee.objects.create(name='Вероника', birth_date='1678-08-19', position='Тех поддержка', salary='100000',
                               work_experience=4)
emp3 = Employee.objects.create(name='Элнур', birth_date='2005-03-14', position='Универсал', salary='40000',
                               work_experience=3)
emp4 = Employee.objects.create(name='Кубат', birth_date='2004-02-13', position='Посудомойщик', salary='10000$',
                               work_experience=12)


passforemp1 = Passport.objects.create(inn='23564568976543', id_card='2276532', employee=emp1)
passforemp2 = Passport.objects.create(inn='12387654768543', id_card='8765432', employee=emp2)
passforemp3 = Passport.objects.create(inn='27865647899432', id_card='9976545', employee=emp3)
passforemp4 = Passport.objects.create(inn='29987654657321', id_card='2276588', employee=emp4)

last_employee = Employee.objects.last()
last_employee.delete()


word_project = WorkProject.objects.create(project_name='Хакатон')
word_project.members.set([emp1, emp2, emp3], through_defaults={'date_joined': '2020-03-17'})
word_project.members.remove(emp3)
word_project.members.create(name='Темирлан',
                            birth_date='2004-07-14',
                            position='Менеджер',
                            salary='60000',
                            work_experience=4,
                            through_defaults={'date_joined': '2020-07-22'})


person1 = Client.objects.create(name='Али', birth_date='2004-07-15', address='Асанбай центр', phone_number='0500898769')
person = Client.objects.create(name='Жанат', birth_date='2004-09-26', address='Гум', phone_number='0999765643')
person3 = Client.objects.create(name='Бегимай', birth_date='2003-08-02', address='Джал', phone_number='0777718778')

person3del = Client.objects.filter(name='Бегимай')
person3del.delete()

Employee.objects.all()
Passport.objects.all()
WorkProject.objects.all()
Membership.objects.all().first() или Membership.objects.filter(member=emp1)
Client.objects.all()
VIPClient.objects.all()

exit()
