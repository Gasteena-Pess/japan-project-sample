import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an interviewer for a technical role at IT company"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "AI interviewer")

demo.launch(share=True)