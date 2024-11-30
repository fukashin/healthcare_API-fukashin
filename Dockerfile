# Pythonの公式イメージを使用
FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なシステムパッケージをインストールあ
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y dnsutils iputils-ping curl
RUN apt-get update && apt-get install -y postgresql-client

# 必要なファイルをコピー
COPY requirements.txt .

# パッケージのインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# プロジェクトのソースコードをコピー
COPY . .


ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=adminpassword
# スーパーユーザー作成を実行
RUN python create_superuser.py || true

# ポート8000を開放
EXPOSE 8000

# Djangoサーバーを起動
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
