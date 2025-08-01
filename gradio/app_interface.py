import gradio as gr

""""
This is a text customizer
It customizes the text with color, size and font style
"""


def customize_text(text, background_color, text_color, font_size, font_style):
    estilo = (
        f"color: {text_color}; "
        f"background-color: {background_color}; "
        f"font-size: {font_size}px; "
        f"font-family: {font_style};"
    )
    return f'<div style="{estilo}">{text}</div>'


iface = gr.Interface(
    fn=customize_text,
    inputs=[
        gr.Textbox(label="Text", placeholder="Enter your text here..."),
        gr.ColorPicker(label="Background Color"),
        gr.ColorPicker(label="Text Color"),
        gr.Slider(minimum=10, maximum=100, label="Font Size", value=20),
        gr.Radio(
            choices=["Arial", "Courier New", "Georgia", "Times New Roman", "Verdana"],
            label="Font Style",
        ),
    ],
    outputs=gr.HTML(label="Customized Text"),
    title="Text Customizer",
    description="Customize your text with color, size and font style.",
)

iface.launch()
