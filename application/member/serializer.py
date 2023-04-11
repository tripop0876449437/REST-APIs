from rest_framework import serializers
from member.models import Member
from member.models import Reward, RewardHistory

class CreateMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class CreateRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'

# class CreateRewardHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RewardHistory
#         fields = '__all__'
class CreateRewardHistorySerializer(serializers.ModelSerializer):
    member_id = CreateMemberSerializer(many=False,read_only=True)
    reward_id = CreateRewardSerializer(many=False,read_only=True)
    class Meta:
        model = RewardHistory
        fields = '__all__'
