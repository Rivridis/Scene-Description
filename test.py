import threading
import time
from tkinter import Tk, Label
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize Tkinter window
root = Tk()
root.title("Generated Caption")
root.geometry("500x300")

# Label for displaying captions
caption_label = Label(root, text="Generating...", font=("Arial", 14), wraplength=400)
caption_label.pack(pady=20)

# Load the BLIP model and processor
path = r"venv\\models--Salesforce--blip-image-captioning-base\\snapshots\\82a37760796d32b1411fe092ab5d4e227313294b\\"
processor = BlipProcessor.from_pretrained(path)
model = BlipForConditionalGeneration.from_pretrained(path)

def generate_caption(img="Who.png"):
    """Generates a caption for the given image."""
    try:
        image = Image.open(img)
        inputs = processor(images=image, return_tensors="pt")
        caption = model.generate(**inputs)
        return processor.decode(caption[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error: {str(e)}"

def update_caption():
    """Updates the caption label every 2 seconds."""
    caption_text = generate_caption()
    caption_label.config(text=caption_text)
    root.after(2000, update_caption)  # Schedule next update

def start_caption_thread():
    """Runs caption updates in a separate thread."""
    threading.Thread(target=update_caption, daemon=True).start()

# Start the caption generation in a separate thread
start_caption_thread()

# Run Tkinter event loop
root.mainloop()