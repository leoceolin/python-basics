import gradio as gr

""""
This is a data processor
It processes the data with text, number, image, list of text, color and options
It also reverses the text, doubles the number, checks if the image is received and processes the list of text
It also returns the selected color and the options
"""


def process_data(text, number, image, list_text, color, options):
    reversed_text = text[::-1]
    double_number = number * 2
    image_message = "Image received!" if image else "No image received"

    processed_list = [[item] for item in list_text.splitlines()] if list_text else []

    return (
        reversed_text,
        double_number,
        image_message,
        processed_list,
        f"Selected color: {color}",
        options,
    )


iface = gr.Interface(
    fn=process_data,
    inputs=[
        gr.Textbox(label="Text", placeholder="Enter a text here..."),
        gr.Slider(minimum=0, maximum=100, label="Number", value=0),
        gr.Image(type="pil", label="Image"),
        gr.Textbox(label="List of items", lines=4, placeholder="Item1\nItem2"),
        gr.ColorPicker(label="Select a color"),
        gr.CheckboxGroup(
            choices=["Option 1", "Option 2", "Option 3"], label="Choose your options"
        ),
    ],
    outputs=[
        gr.Textbox(label="Reversed text"),
        gr.Number(label="Double the number"),
        gr.Textbox(label="Message about the image"),
        gr.DataFrame(label="Items of the list", headers=["Items"]),
        gr.Textbox(label="Selected color"),
        gr.Textbox(label="Selected options"),
    ],
    title="Input and Output Types Checker",
    description="Enter a text, a number, an image, a list of items, a color and options to see how the input is processed",
)

iface.launch()
