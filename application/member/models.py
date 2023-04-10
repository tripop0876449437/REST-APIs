from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    point = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self,):
       return "{0}  {1}".format(self.first_name,self.last_name) 

    

class Reward(models.Model):
    name = models.CharField(max_length=50)
    point = models.IntegerField(default=0)

    def __str__(self,):
       return "{0} : {1}".format(self.name,self.point) 

class RewardHistory(models.Model):
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE)
    reward_id = models.ForeignKey('Reward', on_delete=models.CASCADE)
    point_used = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updatated_at = models.DateTimeField(auto_now=True)

    def __str__(self,):
       return "{0} : {1}".format(self.member_id,self.reward_id) 
