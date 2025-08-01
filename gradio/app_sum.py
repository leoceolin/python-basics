import gradio as gr


def sum_numbers(num1, num2):
    return num1 + num2


"""
This is a simple calculator that adds two numbers
"""

iface = gr.Interface(
    fn=sum_numbers,
    inputs=["number", "number"],
    outputs="number",
    title="Simple Sum Calculator",
    description="Enter two numbers to get the sum",
    theme="default",
)

iface.launch()
