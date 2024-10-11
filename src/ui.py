import gradio as gr

def create_ui(chat_fn):
    theme = gr.themes.Base(
        primary_hue="red",
        secondary_hue="red",
        neutral_hue="slate",
    )

    with gr.Blocks(theme=theme) as demo:
        gr.Markdown("<h1><center>The Daily Pennsylvanian’s SEO Engine</center></h1>")
        gr.Markdown("<div style='text-align: center;'>A project created by DP Business Analytics/div>")

        chatbot = gr.Chatbot()
        title = gr.Textbox(placeholder="Insert article title here", label="Article Title")
        content = gr.Textbox(placeholder="Insert article content here", label="Article Content")
        input_box = gr.Textbox(placeholder="Ask a question!", label="Question")
        dept = gr.Dropdown(["Under the Button", "34th Street", "DP Sports", "DP General"], label="Department", info="Which publication is this article for?", allow_custom_value=True)
        state = gr.State()

        submit = gr.Button("SEND")
        clear = gr.Button("CLEAR")
        reset_chat = gr.Button("RESET CHAT HISTORY")
        gr.Markdown("<a href = 'https://forms.gle/GWXTSeykKMPHm6DY9'><center>Submit Bugs or Feedback Here!</a>")

        submit.click(chat_fn, inputs=[input_box, dept, title, content, state], outputs=[chatbot, state, input_box, dept, title, content])
        clear.click(lambda: ([], None, None, None, [], []), inputs=None, outputs=[chatbot, input_box, dept, title, content, state], queue=False)
        reset_chat.click(lambda: ([]), inputs=None, outputs=[chatbot], queue=False)

    return demo
