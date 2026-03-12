from app import create_app

# app/__init__.py의 create_app()을 실행하여 앱 객체를 만듭니다.
app = create_app()

if __name__ == "__main__":
    # 기존에 사용하던 포트(예: 5000)와 호스트 설정을 유지하세요.
    app.run(host='0.0.0.0', port=5000, debug=True)
