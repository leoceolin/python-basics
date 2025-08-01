import gradio as gr

"""
This is a temperature converter
It converts temperatures between Celsius and Fahrenheit

"""


def convert_temperature(temperatura, escala):
    if escala == "Celsius":
        return (temperatura * 9 / 5) + 32
    else:
        return (temperatura - 32) * 5 / 9


iface = gr.Interface(
    fn=convert_temperature,
    inputs=[
        gr.Number(label="Temperature", precision=2),
        gr.Radio(choices=["Celsius", "Fahrenheit"], label="Convert from"),
    ],
    outputs=gr.Number(label="Result"),
    title="Temperature Converter",
    description="Convert temperatures between Celsius and Fahrenheit",
)

iface.launch()
