from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name="Назва")
    description = models.TextField("Опис")
    url = models.SlugField(max_length=150, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = "Катерогії"

class Tour(models.Model):
    title = models.CharField('Title', max_length=150)
    description = models.TextField("Опис")
    photo = models.ImageField("Фото",upload_to='photos/&Y/%m/&d/')
    country = models.CharField('Країна', max_length=50)
    hotel = models.CharField('Готель', max_length=150)
    category = models.ForeignKey('Category',on_delete=models.PROTECT, null=True, blank=True )
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = "Тури"


class RaitingStart(models.Model):
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Зірка рейтингу'
        verbose_name_plural = "Зірки рейтингу"

class Raiting(models.Model):
    ip = models.CharField('IP адреса', max_length=150)
    star = models.ForeignKey(RaitingStart, on_delete=models.CASCADE, verbose_name="зірка")
    tour = models.ForeignKey(Tour, on_delete=models.CharField,verbose_name='тур')
    def __str__(self):
        return f"{self.star} - {self.title}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Ник', max_length=50)
    text = models.TextField('Текст',max_length=150)
    parent = models.ForeignKey(
    'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )
    tour = models.ForeignKey(Tour, verbose_name='Titile', on_delete=models.CASCADE)



    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = "Відгуки"
