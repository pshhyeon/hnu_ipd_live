from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.http import JsonResponse
# 문자열 해싱
from django.contrib.auth.hashers import make_password
# 해싱한 문자열 비교
from django.contrib.auth.hashers import check_password
# 멀티쓰레딩
from concurrent.futures import ThreadPoolExecutor
from live.dao import DaoLive
import time

def main(request):
    return redirect('/test_page')

def test_page(request):
    return render(request, 'test_page.html')

def door_lock_page(request):
    return render(request, 'door_lock_page.html')

def login_page(request):
    return render(request, 'login_page.html')

@csrf_exempt
def login_act(request):
    u_id = request.POST['id']
    u_password = request.POST['password']
    dl = DaoLive()
    vo = dl.selectUserNum(u_id, u_password)
    return render(request, 'home.html', {'vo':vo})

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def save_password(request):
    # hashed_0000 = make_password("0000")
    # hashed_9999 = make_password("9999")
    # print("0000 해시 암호화:", hashed_0000)
    # print("9999 해시 암호화:", hashed_9999)
    
    if request.method == "POST":
        import json
        data = json.loads(request.body)  # JSON 데이터 파싱
        password = data.get("password")  # 4자리 난수 가져오기

        # 비밀번호 해싱
        hashed_password = make_password(password)

        print(f"원본 비밀번호: {password}")
        print(f"해싱된 비밀번호: {hashed_password}")

        # 세션에서 사용자 정보 가져오기
        # user_num = request.session.get('user_num')  
        # room_no = request.session.get('room_no')
        # 일단 user_num, room_no 하드코딩
        user_num = 2
        room_no = "1001"

        dl = DaoLive()
        newPwdIdVo = dl.selectNewPwdId()
        newPwdId = newPwdIdVo["NEW_PWD_ID"]
        # print("PWD_ID: ", newPwdId)
        cnt = dl.savePassword(hashed_password, newPwdId, user_num, room_no)
        if cnt > 0 : 
            print("저장 성공")
            return JsonResponse({"status": "success", "password": password})  # 응답 반환

    return JsonResponse({"status": "fail", "message": "Invalid request"}, status=400)

def password_list_page(request):
    return render(request, 'password_list_page.html')

def password_page(request):
    return render(request, 'password_page.html')

@csrf_exempt
def password_check(request):
    # e_id = request.POST['e_id']
    # e_name = request.POST['e_name']
    # gen = request.POST['gen']
    # addr = request.POST['addr']
    # de = DaoEmp()
    # cnt = de.update(e_id, e_name, gen, addr)
    # return render(request, 'emp_mod_act.html',{'cnt':cnt})
    u_id = request.POST['number']
    u_password = request.POST['password']
    dl = DaoLive()
    vo = dl.selectUserNum(u_id, u_password)
    return render(request, 'home.html', {'vo':vo})

# 공동현관 도어락 비밀번호 확인 메서드
@csrf_exempt
def door_pass(request):
    start_time = time.time()  # 비밀번호 확인 로직 시작 시간
    room_no = request.GET.get("room_no")
    input_password = request.GET.get("input_password")

    # 입력값 유효성 검사
    if not room_no or not input_password:
        return JsonResponse({"status": "fail", "message": "Missing parameters"}, status=400)

    dl = DaoLive()
    password_list = dl.selectPwdList(room_no)  # 비밀번호 목록 조회
    print("DB 조회 시간:", time.time() - start_time)  # DB에서 데이터를 가져오는 데 걸린 시간 출력

    # 비밀번호 검증 함수 (하나의 비밀번호 검증 로직)
    def verify_password(pwd_info):
        hashed_pwd = pwd_info["PWD"]
        if check_password(input_password, hashed_pwd) and pwd_info["DEL_DT"] is None:  # 검증 조건
            return pwd_info  # 일치하면 해당 데이터를 반환
        return None  # 불일치하면 None 반환

    start_loop = time.time()  # 검증을 위한 반복문 시작 시간

    # ThreadPoolExecutor를 사용해 병렬로 비밀번호 검증
    with ThreadPoolExecutor() as executor:
        # ThreadPoolExecutor는 병렬 작업을 수행하기 위해 스레드 풀을 생성합니다.
        # with 문을 사용하면 작업이 끝난 후 자동으로 리소스를 정리합니다.
        results = list(executor.map(verify_password, password_list)) # 비밀번호 리스트를 병렬로 검증하여 결과 리스트 생성
        """
        executor.map(): 주어진 함수를 여러 입력값에 대해 병렬로 실행합니다.
            첫 번째 인자: verify_password 함수 (검증 로직)
            두 번째 인자: password_list (DB에서 가져온 비밀번호 목록)
        map()의 결과: 각 작업의 반환값을 순서대로 담은 리스트가 생성됩니다.
            verify_password 함수에서 조건이 일치하면 비밀번호 정보를 반환하고, 불일치하면 None을 반환합니다.
        """


    # 결과 처리: 일치하는 비밀번호가 있는지 확인
    for pwd_info in results:
        if pwd_info:  # 일치하는 비밀번호가 존재하면
            print("반복문으로 해싱 검증 시간:", time.time() - start_loop)
            if pwd_info["USE_ONCE_YN"] == "y":  # 일회용 비밀번호인 경우
                dl.updateDelDate(pwd_info["PWD_ID"])  # 비밀번호 삭제 처리
            print("총 처리 시간:", time.time() - start_time)
            return JsonResponse({"status": "success"})  # 성공 응답 반환

    return JsonResponse({"status": "fail"})  # 비밀번호 불일치 시 실패 반환














