from django.db import models

from .utils import from_ru_to_en

class City(models.Model):
    # Charfield string text wthi limited lenght
    # Parameter unigue catch and delete dublicates
    name = models.CharField(max_length=50, verbose_name='Название города', unique=True)
    # blank means that this section maybe empty
    slug = models.CharField(max_length=50, blank=True, unique=True)

    # For changing City title in admin/ before this it is like than City()
    class Meta:
        verbose_name = 'Название города'
        verbose_name_plural = 'Название городов'
    
    # For changing city names /  before this it is like than City.object
    def __str__(self):
        return self.name

    # Redefine slug variable if we not enter anything this function is activate
    # We use super when we want to call function from base class Model ?in our function we call save()
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_ru_to_en(str(self.name))
        super().save(*args,**kwargs)

class Language(models.Model):
    #
    name = models.CharField(max_length=50, verbose_name='Язык программирования', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    # 
    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'
    
    
    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_ru_to_en(str(self.name))
        super().save(*args,**kwargs)

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок вакансии')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Орисание вакансии')
    # We should use DRY rule, and for it we use db properties in our one-to-many
    # foreign_key - it is mean than one object can contain many another objects one city many vacansies
    # on delete define wat we do with many objects if one main object deleted , Cascade also deleted all objecst
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык программирования')

    # Define time when vacancy was add, auto_now_add define auto and add to our model
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Все вакансии'

    def __str__(self):
        return self.title