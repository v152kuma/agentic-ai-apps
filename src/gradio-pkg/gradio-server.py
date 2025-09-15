import gradio as gr

def greet(name, intensity):
    greeting = "Hello, " + name + "!"
    if intensity == "Loud":
        greeting = greeting.upper()
    elif intensity == "Whisper":
        greeting = greeting.lower()
    return greeting

iface = gr.Interface(
    fn=greet,
    inputs=[
        gr.Textbox(label="Name"),
        gr.Slider(minimum=1, maximum=10, step=1, label="Excitement Level"),
        gr.Radio(choices=["Normal", "Loud", "Whisper"], label="Greeting Intensity")
    ],
    outputs=gr.Textbox(label="Greeting"),
    title="Greeting App",
    description="Enter your name and select the intensity of the greeting."
)

iface.launch(server_name="localhost", server_port=7860)