import gradio as gr
import string
from collections import Counter


def analyze_text(texto):
    texto_limpo = texto.translate(str.maketrans("", "", string.punctuation))
    palavras = texto_limpo.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)

    frequencia = Counter(palavras)
    frequencia_html = "<br>".join(
        [f"{palavra}: {contagem}" for palavra, contagem in frequencia.items()]
    )

    return num_palavras, num_caracteres, frequencia_html


iface = gr.Interface(
    fn=analyze_text,
    inputs=[gr.Textbox(label="Text", placeholder="Enter the text here", lines=6)],
    outputs=[
        gr.Number(label="Number of words"),
        gr.Number(label="Number of characters"),
        gr.HTML(label="Word frequency"),
    ],
    title="Text Analyzer",
    description="Enter a text and get analyses about it",
)

iface.launch()
