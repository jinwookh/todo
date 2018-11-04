# todo

# 1. 리눅스에서의 사용법
(1) 파이썬 설치 (python 3.0 이상 설치 권장)

(2) pip install django 를 실행합니다.

(3) 최상위 todo 파일에서
    python manage.py runserver 를 실행합니다.


# 2. aws 배포판 url
http://ec2-54-180-97-158.ap-northeast-2.compute.amazonaws.com:8000/ 

# 3. test 실행 방법
최상위 todo 파일에서
python manage.py test todo 를 실행합니다.

test case는 6가지입니다.

(1) index.html에서 todo object가 없는 경우

(2) index.html로 기한이 만료된 todo가 넘겨진 경우

(3) index.html로 기한이 만료된 todo 하나, 만료되지 않은 todo 하나가 넘겨진 경우

(4) detail.html로 todo 하나가 넘겨진 경우

(5) completedList.html로 넘겨질 completedTodo object가 없는 경우

(6) completedList.html로 넘겨질 completedTodo object가 하나 있는 경우
