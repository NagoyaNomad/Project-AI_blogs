# responce.pyのメイン処理部分をクラス化する

# API KEYを環境変数から呼び出すためにosモジュールを使う。
import os
from openai import OpenAI


class Get_AI_Responce():
    def __init__(self, system_content, user_content):
        # 使用するOpen AIを指定する。
        self._MODEL = "gpt-4o-mini"

        # 使用するAPI KEYをセットして、OpenAIのインスタンスを生成する。
        self._API_KEY = os.environ.get("OPENAI_API_KEY")
        self._client = OpenAI(api_key = self._API_KEY)

        # AIに渡す引数は、インスタンスの引数から渡す。
        self.system_content = system_content
        self.user_content = user_content

    def responce(self):
        # AIメイン処理（古い資料とは参照の仕方が変わっている）
        response = self._client.chat.completions.create(
            model = self._MODEL,
            messages = [
                {'role': 'system', 'content': self.system_content},
                {'role': 'user', 'content': self.user_content},
            ]
        )

        return response.choices[0].message.content



if __name__ == "__main__":
    # AIプロンプト
    system_content = 'あなたは数学の専門家です。'
    user_content = 'ピタゴラスの定理を説明してください。'

    # AIから回答を求めるインスタンスを生成する。
    ai_answer = Get_AI_Responce(system_content, user_content)

    # AIの結果を出力する。
    print('### AIの返答 ###')
    print(ai_answer.responce())
