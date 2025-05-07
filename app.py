from flask import Flask,render_template,request
import random
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('homepage.html')
@app.route('/game',methods=['GET','POST'])
def game():
    result=None
    User_choice=None
    Computer_choice=None
    if request.method=='POST':
        user_choice=request.form['choice']
        options=['rock','paper','scissor']
        Computer_choice=random.choice(options)
        if user_choice == computer_choice:
            result = 'Draw'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = 'You Win!'
        else:
            result = 'Computer Wins!'
    return render_template('game.html',user=user_choice,computer=computer_choice, result=result)
if __name__ == '__main__':
    app.run(debug=True)
