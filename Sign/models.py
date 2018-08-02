from django.db import models


class User(models.Model):
    bduss = models.CharField(max_length=192,verbose_name="BDUSS")
    username = models.CharField(max_length=30,verbose_name="贴吧用户名")
    email = models.EmailField(null=True,verbose_name="邮箱")
    token = models.CharField(max_length=200,unique=True,verbose_name="个人TOKEN")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="提交时间")
    modified_time = models.DateTimeField(auto_now=True,verbose_name="修改时间")
    idDel = models.BooleanField(default=False,verbose_name="是否删除")

    def __str__(self):
        return self.username


class Tieba(models.Model):
    name = models.CharField(max_length=40,verbose_name="贴吧名")
    fid = models.CharField(max_length=20,verbose_name="fid")
    isLou = models.BooleanField(verbose_name="是否楼中楼")
    floor = models.CharField(max_length=20,null=True,verbose_name="楼层号")
    qid = models.CharField(max_length=20,null=True,verbose_name="楼层号编号")
    tbjingyan = models.IntegerField(verbose_name="贴吧经验")
    tbdengji = models.IntegerField(verbose_name="贴吧等级")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="插入时间")
    user = models.ManyToManyField(User,verbose_name="所属用户")

    def __str__(self):
        return self.name





