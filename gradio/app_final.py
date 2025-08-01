import gradio as gr
from collections import Counter
import string

""""
This is a weather report generator
It generates a weather report based on the temperature, scale, condition and text, it also analyzes the text and returns the number of words, characters and word frequency
"""


def convert_temperature(temperature, scale):
    if scale == "Celsius":
        return (temperature * 9 / 5) + 32
    else:
        return (temperature - 32) * 5 / 9


def analyze_text(text):
    clear_text = text.translate(str.maketrans("", "", string.punctuation))
    words = clear_text.split()
    num_words = len(words)
    num_chars = len(text)

    frequency = Counter(words)
    word_frequency = "<br>".join(
        [f"{word}: {count}" for word, count in frequency.items()]
    )

    return num_words, num_chars, word_frequency


def create_report(temperature, scale, condition, text):
    converted_temperature = convert_temperature(temperature, scale)
    num_words, num_chars, word_frequency = analyze_text(text)

    report = (
        f"**Weather Report**\n\n"
        f"Temperature: {converted_temperature:.2f}{'F' if scale=='Celsius' else 'C'}\n"
        f"Condition: {condition}\n"
        f"Description: {text}\n\n"
        f"Number of Words: {num_words}\n"
        f"Number of Characters: {num_chars}\n"
        f"Word Frequency: {word_frequency}\n"
    )

    return report


iface = gr.Interface(
    fn=create_report,
    inputs=[
        gr.Number(label="Temperature", precision=2),
        gr.Radio(choices=["Celsius", "Fahrenheit"], label="Convert from"),
        gr.Dropdown(
            choices=["Sunny", "Cloudy", "Rainy", "Cold", "Hot"],
            label="Weather Condition",
        ),
        gr.Textbox(
            label="Description of the Day", lines=4, placeholder="Describe the day"
        ),
    ],
    outputs=gr.Markdown(label="Weather Report"),
    title="Weather Report",
    description="Create a weather report with temperature",
)

iface.launch()
