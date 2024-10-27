# Pythonの公式イメージを使用
FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# プロジェクトのソースコードをコピー
COPY . .

# ポート8000を開放
EXPOSE 8000

# Djangoサーバーを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
