# OpenAI APIで文章を作成する基本プログラム
# 参考資料 [やすひらブログ：OpenAI APIの使い方, 20250205](https://yasuhira-blog.com/python-openai/)

# API KEYを環境変数から呼び出すためにosモジュールを使う。
import os
import time

from openai import OpenAI

# API Keyを環境変数から読み込む。
API_KEY = os.environ.get("OPENAI_API_KEY")

# 使用するOpen AIを指定する。
MODEL = "gpt-4o-mini"

system_content = 'あなたは数学の専門家です。'
user_content = '正三角形の定義をしてください。'

client = OpenAI(api_key = API_KEY)

# 時間計測
start_time = time.perf_counter()

# AIメイン処理（古い資料とは参照の仕方が変わっている）
response = client.chat.completions.create(
    model = MODEL,
    messages = [
        {'role': 'system', 'content': system_content},
        {'role': 'user', 'content': user_content},
    ]
)

# AIの返答までの時間を算出する。
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"実行時間: {elapsed_time:.2f} 秒")

# AIの結果を出力する。
print('### AIの返答 ###')
print(response.choices[0].message.content)
