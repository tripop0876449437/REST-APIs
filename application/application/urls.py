"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from member.views import MemberView , RewardView , CollectPoint , RewardHistoryView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/request', MemberView.as_view()),
    path('member/add', MemberView.as_view()),
    path('member/<int:member_id>/delete', MemberView.as_view()),
    path('member/<int:member_id>/update', MemberView.as_view()),
    path('member/<int:member_id>/add/point', CollectPoint.as_view()),
    path('reward/request', RewardView.as_view()),
    path('reward/add', RewardView.as_view()),
    path('reward/redeem', RewardHistoryView.as_view()),
    path('reward/<int:reward_id>/delete', RewardView.as_view()),
    path('reward/<int:reward_id>/update', RewardView.as_view()),
    path('reward_history/request', RewardHistoryView.as_view()),
]
