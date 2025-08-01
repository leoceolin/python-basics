import gradio as gr
import math

""""
This is a factorial calculator
It calculates the factorial of a number
"""


def factorial(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    return math.factorial(num)


iface = gr.Interface(
    fn=factorial,
    inputs="number",
    outputs="text",
    title="Factorial Calculator",
    description="Enter a number to get the factorial",
)

iface.launch()
