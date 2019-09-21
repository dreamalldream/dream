from django.db import models

# Create your models here.
class Book(models.Model):
    # 定义属性:默认主键自增id字段可不写
    title = models.CharField(max_length=20,verbose_name="书籍名称")
    pub_date = models.DateTimeField(verbose_name="书籍出版日期")
    # 定义默认输出格式
    def __str__(self):
        return  self.title
    # 自定义对应的表名,默认表名:bookApp_book
    class Meta:
        db_table = "books"
        verbose_name = '图书信息'
        # 复数时显示的名称
        verbose_name_plural = '图书信息'
class Hero(models.Model):
    name = models.CharField(max_length=20,verbose_name="姓名")
    gender = models.BooleanField(verbose_name="性别")
    content = models.CharField(max_length=100,verbose_name="详情")
    Book = models.ForeignKey('Book', on_delete=False,verbose_name="所属书籍")
    def __str__(self):
        return  self.name
    # 自定义对应的表名,默认表名:bookApp_hero
    class Meta:
        db_table = "heros"
        verbose_name = "人物信息"
        verbose_name_plural = "人物信息"
    def sex(self):
        if self.gender:
            return  "男"
        else:
            return  "女"
