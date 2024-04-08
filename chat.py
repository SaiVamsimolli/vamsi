import openai
from toolkit import texttospeech as tts
openai.api_key = ""
openai.api_base = "https://api.pawan.krd/pai-001-light-beta/v1"

print("Hi there! I'm PAI bot. How can I assist you today?")
user_input=input("user : ")
while user_input.lower() != "bye":
    response = openai.ChatCompletion.create(
        model="pai-001-light-beta",
        messages=[
            {'role': 'user', 'content': user_input},
        ],
        stream=True,
     allow_fallback=True
    )
    print("friday : ")
    for chunk in response:
        print(chunk.choices[0].delta.get("content", ""), end="", flush=True)
        tts.txtToSpeech(chunk.choices[0].delta.get("content", ""))
    user_input=input("\nuser : ")
    
