from .models import Mission

def mission_create():
    print("mission함수 실행!!!!!!!!!!!!")
    content_list = [
        '이 강민성한테 욕하게 하기',
        '랑 팔씨름 해서 이기기',
        '게다리 춤 시키기',
        '같이 포켓몬스터 노래 부르기',
        '상세한 집주소 알아내기',
        '집에 같이 가자는 각서 받아내기',
        '의 친구랑 통화하기(나는 기존에 모르던)',
        '의 머리카락 뽑아서 보관하기',
        '에게 떨어진 음식 먹이기',
        '첫사랑 이름 알아오기',
        '부모님 두 분 다 띠 알아오기',
        '코에다가 점찍기',
        '(이)랑 3분 이상 통화하기',
        '빼고 단체사진 찍기',
    ]

    for content in content_list:
        Mission.objects.create(content=content)

