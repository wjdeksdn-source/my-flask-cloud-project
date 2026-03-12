FROM python:3.9-slim

WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 전체 소스 복사 (api, board, news, __init__.py 포함)
COPY . .

# Flask 실행 (Gunicorn 권장)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
