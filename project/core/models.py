from django.db import models
from django.contrib.auth.models import User



class Mission(models.Model):
    content = models.TextField(max_length=100)
    flag = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content

class Member(models.Model):
    name = models.CharField(max_length=3)
    managerFlag = models.BooleanField(default=False)
    manitoFlag = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.CharField(max_length=1)
    manito = models.OneToOneField(Member, on_delete=models.PROTECT)
    mission = models.OneToOneField(Mission, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username

    # 유저가 지워지면 해당 maito와 mission 을 다시 활성화 시키자
    # def __del__(self):
    #     print("소멸자 실행!!!!!!!!!!!!")
    #     self.manito.manitoFlag = False
    #     self.mission.flag = False
    #     self.manito.save()
    #     self.mission.save()
        



