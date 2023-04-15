import openai
import requests
from pprint import pprint
from typing import List
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
KEY = ""
openai.api_key = KEY
app.secret_key='key'

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
users = dict()


@app.route('/set_session', methods=['POST'])
def set_session():
    # username = request.form['username']
    username = request.cookies.get('username')
    print(f'Username from resquest.cookies : {username}')
    messages = [{"role": "system",
                 "content": "Act as Walmart chatbot and response to user query only with reference to Walmart.."}]
    if username not in users:
        print(f'New session created for {username}')
        users[username] = {'session': session, 'chat_history': messages}
    return jsonify({'message': 'Session is set for ' + username})


def ask_question(txt):
    # messages = [{"role": "system",
    #              "content": "Act as Walmart chatbot and response to user query only with reference to Walmart.."}]
    username = request.cookies.get('username')
    print('username in ask_question method ',username)
    chat_history = []
    print("still inside ask_question")
    if username:
        print("still inside ask_question inside if username")
        session['username'] = username
        print('session is set for the username :', username)
        chat_history = users[username].get('chat_history', [])
        print("still inside ask_question inside if username chat_history ", chat_history)
    else:
        # chat_history=[]
        print('session is not set for the username :', username)

    chat_history.append({"role": "user", "content": txt})
    print("2:", txt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    answer = response.choices[0].message.content.strip()
    chat_history.append({"role": "assistant", "content": answer})
    print("3:", txt)
    users[username]['chat_history'] = chat_history
    print("4:", users[username]['chat_history'])
    return answer


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/api', methods=['POST'])
def process_message():
    userInput = request.json['message']
    print("userInput :" + userInput)
    # Here you can process the user input and generate a response using OpenAI or any other library
    response = ask_question(userInput)
    return jsonify({"message": response})


if __name__ == '__main__':
    app.run(debug=True)

#
# KEY="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"
# openai.api_key =KEY
#
# start_sequence = "\nA:"
# restart_sequence = "\n\nQ: "
#


# if userInput == "exit":
#     break
#
# # Example usage
#
