# 🦁 여름학기 멋쟁이사자처럼 12기 세션

## 🌟 DRF (Django Restful Framework) 배우기

안녕하세요! 이 리포지토리는 여름학기 멋쟁이사자처럼 12기 세션에서 Django Restful Framework(DRF)를 배우기 위한 개인 학습 자료입니다. DRF는 Django를 사용하여 강력하고 유연한 RESTful API를 쉽게 구축할 수 있게 도와줍니다.

## 🛠️ 설치 방법

1. 이 리포지토리를 클론합니다:
    ```bash
    git clone https://github.com/pyeree/likelion_drf_hw.git
    cd likelion_drf_hw
    ```

2. 가상환경을 생성하고 활성화합니다:
    ```bash
    python -m venv venv
    source venv/bin/activate  # MacOS/Linux
    venv\Scripts\activate  # Windows
    ```

3. 필요한 패키지를 설치합니다:
    ```bash
    pip install -r requirements.txt
    ```

4. 데이터베이스를 마이그레이션합니다:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. 개발 서버를 실행합니다:
    ```bash
    python manage.py runserver
    ```

## 🚀 사용법

- API 엔드포인트에 접근하여 데이터를 조회하거나 수정할 수 있습니다.
- Postman과 같은 도구를 사용하여 API 요청을 테스트할 수 있습니다.
- 브라우저에서 직접 API 엔드포인트를 방문하여 JSON 응답을 확인할 수 있습니다.

## 📝 예제 JSON 데이터
### Singer
```json
{
    "content": "DAY6 is a South Korean rock band formed by JYP Entertainment.",
    "debut": "2015-09-07"
}
