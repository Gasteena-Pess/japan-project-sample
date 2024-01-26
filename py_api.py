'''import openai

openai.api_key = 'pk-mHkYGkBUuIUxsCDyaRTFIICDsKclRCMxjEbincgJrKjhQaf'
openai.api_base = 'https://api.pawan.krd/v1'


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Human: Hello\nAI:",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["Human: ", "AI: "]
)

print(response.choices[0].text)'''
import openai
from prompt_toolkit.shortcuts import prompt

my_API = 'pk-mHkYGkBUuIUxsCDyaRTFIICDsKclRCMxjEbincgJrKjhQaf'
# Load your API key from an environment variable or secret management service
openai.api_key = 'my_API'


def get_response(prompts: list, model="gpt-3.5-turbo"):
  responses = []

  restart_sequence = "\n"

  for item in prompts:
    response = openai.Completion.create(
      model=model,
      messages=[{'role': "user", 'content': prompt}],
      temperature=0,
      max_tokens=20,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    responses.append(response['choices'][0]['message']['content'])

  return responses