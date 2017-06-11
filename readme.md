
#파이썬 웹프로그래밍 관련 실습

 - 관련 라이브러리 설치
pip install django
pip install MySQL-python

 - 디비 마이그레이션 관련
python manage.py makemigrations
python manage.py migrate

 - 앱관련 생성
python manage.py startapp bookmark
python manage.py startapp blog

 - 개발 서버 실행
python manage.py runserver

 - 어드민 관련 계정 생성
python manage.py createsuperuser

 - 내 개인 로컬에서 셋팅
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv chap01

 - 파이썬 메니저 호출창
 alt + r