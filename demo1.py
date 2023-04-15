import os
import openai

KEY=""
openai.api_key =KEY

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "


def ask_question():
    messages = [{"role": "system", "content": "Act as Walmart chatbot and response to user query only with reference to Walmart.."}]
    while True:
        userInput = input("Enter your query:")
        messages.append({"role": "user", "content": userInput})

        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
        )

        # print(response)
        answer = response.choices[0].message.content.strip()
        messages.append({"role": "assistant", "content": answer})
        print(answer)

        if userInput == "exit":
            break

# Example usage

ask_question()
