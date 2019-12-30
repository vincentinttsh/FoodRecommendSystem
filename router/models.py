from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name = '餐廳類別'
        verbose_name_plural = '餐廳類別'
    name = models.CharField(max_length=25, blank=False, verbose_name="類別名稱")

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    class Meta:
        db_table = "restaurants"
        verbose_name = '餐廳'
        verbose_name_plural = '餐廳'
    name = models.CharField(max_length=50, blank=False, verbose_name="餐廳名稱")
    address = models.TextField(
        max_length=255, blank=False, verbose_name="餐廳位置")
    phone = models.CharField(max_length=50, blank=True, verbose_name="餐廳電話")
    time = models.CharField(max_length=50, blank=False, verbose_name="營業時間")
    description = models.TextField(
        max_length=255, blank=True, verbose_name="介紹")
    category = models.ForeignKey('Category', models.CASCADE)

    def __str__(self):
        return self.name


class CommentField(models.Model):
    class Meta:
        db_table = "comments"
        verbose_name = '留言'
        verbose_name_plural = '留言'
    name = models.CharField(max_length=50, blank=False, verbose_name='稱呼')
    grade = models.SmallIntegerField(verbose_name='評分', blank=False)
    comment = models.TextField(verbose_name="評論", blank=False)
    restaurant = models.ForeignKey('Restaurant', models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.grade)


class Suggestion(models.Model):
    class Meta:
        db_table = "suggestion"
        verbose_name = "建議"
        verbose_name_plural = "建議"
    name = models.CharField(max_length=50, blank=False, verbose_name='稱呼')
    email = models.EmailField(blank=False, verbose_name='信箱')
    category = models.CharField(max_length=10, blank=False, verbose_name='類型')
    comment = models.TextField(verbose_name="建議內容", blank=False)
    restaurant = models.ForeignKey('Restaurant', models.CASCADE, null=True)
    handle = models.BooleanField(default=False, verbose_name='是否已處理')

    def __str__(self):
        return self.restaurant.name + " - " + self.category
