from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="姓名")
    sex = models.BooleanField(default=True, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    class_num = models.CharField(max_length=5, verbose_name="班级编号")
    description = models.TextField(max_length=1000, verbose_name="个性签名")

    def pub_date(self):
        return float(self.age)

    pub_date.short_description = "年龄"
    pub_date.admin_order_field = "id"

    class Meta:
        # 设置表名
        db_table = "tb_students"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
