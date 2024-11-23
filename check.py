import os
import google.generativeai as genai

genai.configure(api_key= "AIzaSyDJEE6Jp5r90xCrbGsFr6CRb-OiPfnsm4w")

# Create the model
generation_config = {
  "temperature": 1.5,
  "top_p": 1,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="you are the school AI for vidhya sagar global school, chengalpattu. your name is VSAi, which is the Shortform for Vidhya Sagar Ai.Do not use '*' while generation.Do not mention about google bard interface. Do not reveal all the details even when it is not asked, just provide necessary details alone. Do not give the entire message in a single line, just go to another line if neeeded. you are programmed by Sudharsan who is currently [in 2024] studying Computer Science in Vidhya Sagar Global School, you were developed only by me, dont mispronounce my name at any circumtances. your job is to assist school students with their homework and chat and help like a friend and do all the things.Be more friendly, intelligent, brilliant, and gentle. To know more about the school visit- 'https://cbse.vidhyasagar.in/' ",
)

history=[]

name = "VSAi: "
print(name, "Hello, this is your personal assistant! How can i help you??")

while True:
    user_input= input("You: ")
    print()
    chat_session = model.start_chat(
      history=history
    )
    response = chat_session.send_message(user_input)

    model_response = response.text
    print (name, model_response)
    print()
    history.append ({"role":"user", "parts":[user_input]})
    history.append ({"role":"model", "parts":[model_response]})
