class BlogContent():
    def __init__(self, item, request, response, htmlformat):
        self.item = item
        self.request = request
        self.response = response
        self.htmlformat = htmlformat

    def get_format_content(self):
        if(self.item != "タイトル"):
            return f'<{self.htmlformat}>{self.response}</{self.htmlformat}>'
        else:
            return self.response


if __name__ == "__main__":
    import response_class

    system_content = 'あなたは日本の数学者です。'

    title = ''
    blog_content_list = [
        BlogContent('タイトル', '一次方程式の解法についてのブログのタイトルを１つだけ考えてください。', '', ''),
        BlogContent('リード文', 'のリード文を考えてください。', '', 'p'),
        BlogContent('結論', 'のまとめを考えてください。', '', 'p'),
    ]

    for blog_content in blog_content_list:
        user_content = title + blog_content.request
        ai_answer = response_class.Get_AI_Responce(system_content, user_content)
        blog_content.response = ai_answer.response()

        if blog_content.item == "タイトル":
            title = blog_content.response.replace('\n', '')

        print(user_content)

    print('------------------------')

    # レスポンスの内容をhtml形式で出力する。
    for blog_content in blog_content_list:
        print(blog_content.get_format_content())
