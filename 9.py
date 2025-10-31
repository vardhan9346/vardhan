import openai

openai.api_key = "sk-770jvemfq958iuo5rppaq7351b6lfjtj7dug6ly9qevvobjc"

messages = []

system_msg = input("What type of chatbot would you like to create?\n")

messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type your query.")

while True:
    message = input()
    if message.lower() == "quit":
        break
    messages.append({"role": "user", "content": message})
    response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    reply = response.choices[0].message["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
