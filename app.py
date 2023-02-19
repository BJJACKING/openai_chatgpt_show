# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request, session, redirect, url_for
from openai_txt_gen import get_openai_txt
from openai_image_gen import get_openai_image

app = Flask(__name__, template_folder="templates")
app.secret_key = '888'


@app.route('/')
def chat():
    """
    http://127.0.0.1:5000
    :return:
    """
    return render_template("chat.html")  # 加入变量传递


@app.route('/html_txt', methods=['POST', 'GET'])
def html_txt_gen_by_openai():
    """
    http://127.0.0.1:5000/txt?query="今天星期几"
    :return:
    """
    print("正在对话中，请稍后。。。")
    if request.method == 'POST':
        query = request.form['ask']  # 获取姓名文本框的输入值
        print("query: {}".format(query))
        ans = get_openai_txt(query)
        # ans = "我是一个学生。"
        if ans != "":
            print("ans: {}".format(ans))
            session['ask'] = query
            session['ans'] = ans  # 使用session存储方式，session默认为数组，给定key和value即可
            return redirect(url_for('chat'))  # 重定向跳转到首页
        else:
            return 'the username or userpwd does not match!'


@app.route('/txt')
def txt_gen_by_openai():
    """
    http://127.0.0.1:5000/txt?query="今天星期几"
    :return:
    """
    query = request.args.get('query', default="你好")
    print("正在对话中，请稍后。。。")
    return get_openai_txt(query)


@app.route('/html_image', methods=['POST', 'GET'])
def html_image_gen_by_openai():
    """
    http://127.0.0.1:5000/image?query="夏天的美景"
    :return:
    """
    print("正在对话中，请稍后。。。")
    if request.method == 'POST':
        query = request.form['query']  # 获取姓名文本框的输入值
        print("query: {}".format(query))
        img_url = get_openai_image(query)
        # ans = "我是一个学生。"
        if img_url != "":
            print("img_url: {}".format(img_url))
            session['query'] = query
            session['img_url'] = img_url  # 使用session存储方式，session默认为数组，给定key和value即可
            return redirect(url_for('chat'))  # 重定向跳转到首页
        else:
            return 'the username or userpwd does not match!'


@app.route('/image')
def image_gen_by_openai():
    """
    http://127.0.0.1:5000/image?query="夏天的美景"
    :return:
    """
    query = request.args.get('query', default="冬天的美景")
    return get_openai_image(query)


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5000)
    # app.run(port=5000, host="127.0.0.1", debug=True)
