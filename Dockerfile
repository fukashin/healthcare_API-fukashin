# Pythonの公式イメージを使用
FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y iputils-ping

# 必要なファイルをコピー
COPY requirements.txt .

# パッケージのインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# プロジェクトのソースコードをコピー
COPY . .

# スーパーユーザー作成を実行
RUN python create_superuser.py || true

# ポート8000を開放
EXPOSE 8000

# Djangoサーバーを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
