from django.shortcuts import render
from .models import Member , Reward ,RewardHistory
from rest_framework.views import APIView
from .serializer import CreateMemberSerializer
from .serializer import CreateRewardSerializer,CreateRewardHistorySerializer
from rest_framework.response import Response


class MemberView(APIView):
    ## query
    def get(self,request):
        member = Member.objects.all()
        serializer_class = CreateMemberSerializer
        if not member:
            return Response({"status_code":400, "message":"member not found"})
        else:
            return Response({"data": CreateMemberSerializer(member, many=True).data})

    ## create
    def post(self,request):
        serializer = CreateMemberSerializer(data=request.data)
        if serializer.is_valid():
            
            ## create member
            serializer.save()

            return Response({
            "status_code":200,
            "message":"create success"
            })
        else:
            return Response({
            "status_code":400,
            "error":serializer.errors
            })

    ## update
    def put(self,request,member_id):
        ## orm django
        member = Member.objects.filter(id=member_id).first()
        if not member:
            return Response({
            "status_code":400,
            "message":"member is not found"
            })
        else:
            member.first_name = request.data["first_name"]
            member.last_name = request.data["last_name"]
            member.save()

            return Response({
            "status_code":200,
            "message":"update success"
            })

    ## detele
    def delete(self,request,member_id):
        
         ## orm django
        member = Member.objects.filter(id=member_id).first()
        if not member:
            return Response({
            "status_code":400,
            "message":"member is not found"
            })
        else:
            member.delete()

            return Response({
            "status_code":200,
            "message":"delete success"
            })

class CollectPoint(APIView):
    ## add point to member
    def put(self,request,member_id):
        member = Member.objects.filter(id=member_id).first()
        if not member:
            return Response({
            "status_code":400,
            "message":"member is not found"
            })
        else:
            member.point = request.data["point"]
            member.save()

            return Response({
            "status_code":200,
            "message":"add point to member success"
            })




class RewardView(APIView):
    ## query
    def get(self, request):
        reward = Reward.objects.all()
        serializer_class = CreateRewardSerializer
        if not reward:
            return Response({"status_code":400, "message":"reward not found"})
        else:
            return Response({"data": CreateRewardSerializer(reward, many=True).data})

    ## create
    def post(self, request):
        serializer = CreateRewardSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status_code":200, "message":"create success"})
        else:
            return Response({"status_code":400, "error":serializer.errors})

    ## update
    def put(self,request,reward_id):
        ## orm django
        reward = Reward.objects.filter(id=reward_id).first()
        if not reward:
            return Response({
            "status_code":400,
            "message":"reward is not found"
            })
        else:
            reward.name = request.data["name"]
            reward.point = request.data["point"]
            reward.save()

            return Response({
            "status_code":200,
            "message":"update success"
            })

    ## delte
    def delete(self,request,reward_id):
        reward = Reward.objects.filter(id=reward_id).first()

        if not reward:
            return Response({"status_code":400, "message":"reward is not found"})
        else:
            reward.delete()
            return Response({"status_code":200,"message":"delete success"})
    

class RewardHistoryView(APIView):
    ## query
    def get(self, request):
        reward_history = RewardHistory.objects.all()
        serializer_class = CreateRewardHistorySerializer
        if not reward_history:
            return Response({"status_code":400, "message":"reward not found"})
        else:
            return Response({"data": CreateRewardHistorySerializer(reward_history, many=True).data})



    def post(self,request):
        ## orm django
        member = Member.objects.filter(id=request.data["member_id"]).first()
        if not member:
            return Response({
            "status_code":400,
            "message":"member is not found"
            })
        else:
            reward = Reward.objects.filter(id=request.data["reward_id"]).first()
            if not reward:
                return Response({
                    "status_code":400,
                    "message":"reward is not found"
                })
            
            member_point = member.point
            reward_point = reward.point
            

            if member_point >= reward_point:
                ## True
                redeem = RewardHistory.objects.create(
                    member_id = member,
                    reward_id = reward,
                    point_used = reward_point
                )

                ## แลกของรางวัลสำเร็จ
                if redeem:
                    member.point = member_point - reward_point
                    member.save()

            else:
                return Response({
                    "status_code":400,
                    "message":"คะแนนไม่เพียงพอ"
                })


        return Response({
            "status_code":200,
            "message":"redeem success"
        })