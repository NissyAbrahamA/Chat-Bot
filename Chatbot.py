import openai

openai.api_key = "secret key here" # api paywalled

def converse_with_ai(prompt):
    ai_response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Opt for gpt-4 if your plan permits
        messages=[{"role": "user", "content": prompt}]
    )
    return ai_response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        ai_reply = converse_with_ai(user_input)
        print("AI: ", ai_reply)
