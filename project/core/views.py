from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Profile, Member, Mission
from random import *


# Create your views here.
def main(request):
    return render(request, "core/main.html")

def signup(request):
    username_list = []
    member_list = Member.objects.all()
    for member in member_list:
        username_list.append(member.name)

    # username_list = ["이성빈","문범우","왕지영","이신형","이종훈","장관우","장다래","정재인","조윤지","주현도","최용석","이현석","신민정","최혜린"]
    # manito_list = ["이성빈","문범우","왕지영","이신형","이종훈","장관우","장다래","정재인","조윤지","주현도","최용석","이현석","신민정","최혜린"]
    # manager_list = ["강민성","신민정","최혜린"]
    if request.method == "POST":

        username = request.POST["username"]
        if username in username_list:
            password = request.POST["password1"]
            if password == request.POST["password2"]:
                

                # 팀짜기
                member = Member.objects.get(name=username)
                if member.managerFlag:
                    team = "manager"

                else:
                    aNum = Profile.objects.filter(team="A").count()
                    bNum = Profile.objects.filter(team="B").count()
                    if aNum == 6:
                        team = "B"
                    elif bNum == 6:
                        team = "A"
                    else:
                        team_list = ["A", "B"]
                        randomNum = randint(0,1)
                        team = team_list[randomNum]

                # 마니또 뽑기
                manito_list = Member.objects.filter(manitoFlag=False)
                manito = choice(manito_list)
                while manito.manitoFlag | (manito.name == username):
                    manito = choice(manito_list)
                manito.manitoFlag = True
                manito.save()
                

                # 미션 뽑기
                mission_list = Mission.objects.filter(flag=False)
                mission = choice(mission_list)
                while mission.flag:
                    mission = choice(mission_list)
                mission.flag = True
                mission.save()
                

                # user, profile 생성
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                profile = Profile(user=user,team=team, manito=manito, mission=mission)
                profile.save()
                auth.login(request,user)
                return redirect('core:main')

            else:
                # 비밀번호가 틀릴 때 
                messages.info(request, "비밀 번호를 똑같이 적어야 하지 않을까?")
                redirect('core:signup')

        else:
            # username 이 없을 때
            messages.info(request, "본인 이름 석자로 하라고 했는데 말이지...?")
            redirect('core:signup')
    return render(request, "core/signup.html")
        
        


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('core:main')
        else:
            messages.info(request, "한 번에 좀 합시다잉?")
            return redirect('core:login')

    return render(request, "core/login.html")

def logout(request):
    auth.logout(request)
    return redirect('core:login')