from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline
import time
import tkinter as tk
import threading
import pyttsx3
from PIL import Image

checkpoint = r"C:\Users\sanja\.cache\huggingface\hub\models--MBZUAI--LaMini-Flan-T5-248M\snapshots\4e871ba5f20216feaa3b845fc782229cd64eba47"

model2 = pipeline('text2text-generation', model = checkpoint)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
path = r"venv\\models--Salesforce--blip-image-captioning-base\\snapshots\\82a37760796d32b1411fe092ab5d4e227313294b\\"

processor = BlipProcessor.from_pretrained(path)
model = BlipForConditionalGeneration.from_pretrained(path)


style_prompts = {
    "formal": "Make this a formal image caption: ",
    "poetic": "Rewrite this caption in a poetic way: ",
    "funny": "Make this a funny caption: ",
    "detailed": "Rewrite this caption in a detailed way: ",
    "minimal": "Make this as short and minimal as possible: "
}


current_style = "poetic" 

def update_style(selected):
    global current_style
    print(selected)
    current_style = selected

def generate(img="frame.jpg"):
    def run():
        while True:
            image = Image.open(img)

            inputs = processor(images=image, return_tensors="pt")
            caption = model.generate(**inputs)
            caption_text = processor.decode(caption[0], skip_special_tokens=True)
            
            print(caption_text)
            input_prompt = style_prompts[current_style] + caption_text
            generated_text = model2(input_prompt, max_length=512, do_sample=True)[0]['generated_text']
            print(generated_text)
        
            root.after(0, caption_label.config, {"text": generated_text})
            engine.say(caption_text)
            engine.runAndWait()

    root = tk.Tk()
    root.title("Image Caption Generator")
    root.geometry("600x400")  
    root.configure(bg="#E3F2FD") 
    style_selector_var = tk.StringVar()
    style_selector_var.set(current_style)

    caption_label = tk.Label(root, text="Generating Caption...", font=("Arial", 16, "bold"), 
                             wraplength=500, bg="#E3F2FD", fg="#0D47A1", justify="center")
    caption_label.pack(pady=50, padx=20) 
    style_options = list(style_prompts.keys())

    style_menu = tk.OptionMenu(root, style_selector_var, *style_options,command=update_style)
    style_menu.config(font=("Arial", 12), bg="#BBDEFB", fg="#0D47A1")
    style_menu.pack(pady=10)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()

    root.mainloop()


