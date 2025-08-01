import gradio as gr

"""
This is a text reverser
It reverses the text and counts the characters
"""


def reverse_text(texto):
    texto_revertido = texto[::-1]
    return texto_revertido, len(texto_revertido)


iface = gr.Interface(
    fn=reverse_text,
    inputs="text",
    outputs=["text", "number"],
    title="Reversor de Texto",
    description="Insira um texto para revertê-lo e contar os caracteres",
)

iface.launch()
