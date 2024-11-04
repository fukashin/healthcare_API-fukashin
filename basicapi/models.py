# models.py

# Djangoのモデルを作成するために使用するモジュールをインポート
from django.db import models


# profileクラスを定義し、Djangoのモデルを継承してデータベースのテーブルとして扱う
class profile(models.Model):
    # 患者の名を保存する文字列フィールド、最大長は50文字
    first_name = models.CharField(max_length=50)
    # 患者の姓を保存する文字列フィールド、最大長は50文字
    last_name = models.CharField(max_length=50)
    # 患者の年齢を保存する整数フィールド
    age = models.IntegerField()
    # レコードの作成日時を自動で記録する日付と時刻のフィールド
    created_at = models.DateTimeField(auto_now_add=True)
    # モデルインスタンスを文字列として表示するときの表現を定義
    def __str__(self):
        # 患者のフルネームを返す
        return f"{self.first_name} {self.last_name}"
