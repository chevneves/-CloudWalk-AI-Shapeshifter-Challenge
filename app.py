import gradio as gr
from rag_pipeline import answer_question

def chatbot_interface(question):
    return answer_question(question)

iface = gr.Interface(fn=chatbot_interface, inputs="text", outputs="text", title="CloudWalk Chatbot")
iface.launch()
