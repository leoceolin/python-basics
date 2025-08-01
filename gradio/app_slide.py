import gradio as gr
import numpy as np
from PIL import Image
import io
import base64

""""
This is a slide creator
It creates a slide with a title, text, image and background color
"""


def create_slide(title, text, image, background_color, text_color):
    estilo = (
        f"background-color: {background_color}; "
        f"color: {text_color}; "
        "padding: 20px; "
        "text-align: center;"
    )

    # Converte a imagem para base64 se estiver presente
    image_html = ""
    if image is not None:
        buffered = io.BytesIO()
        Image.fromarray(image).save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        image_html = (
            f"<img src='data:image/png;base64,{img_str}' "
            "style='max-width: 100%; height: auto;'>"
        )

    slide_html = f"""
        <div style="{estilo}">
            <h1>{title}</h1>
            <p>{text}</p>
            {image_html}
        </div>
    """
    return slide_html


iface = gr.Interface(
    fn=create_slide,
    inputs=[
        gr.Textbox(label="Title", placeholder="Enter the title.."),
        gr.Textbox(label="Text", placeholder="Enter the text.."),
        gr.Image(type="numpy", label="Image"),
        gr.ColorPicker(label="Background Color"),
        gr.ColorPicker(label="Text Color"),
    ],
    outputs=gr.HTML(label="Customized Slide"),
    title="Slide Creator",
    description="Create a slide with a title, text, image and background color",
)

iface.launch()
