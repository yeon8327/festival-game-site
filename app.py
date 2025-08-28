from flask import Flask, render_template

app = Flask(__name__)

# 메인 페이지 (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# 게임 페이지들
@app.route('/game1')
def game1():
    return render_template('game1.html')

@app.route('/game2')
def game2():
    return render_template('game2.html')

@app.route('/game3')
def game3():
    return render_template('game3.html')

@app.route('/game4')
def game4():
    return render_template('game4.html')

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)
