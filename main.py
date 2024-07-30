import tkinter as tk
from tkinter import filedialog, messagebox
from base64_encoder import base64

class Base64EncoderGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Base64 Encoder/Decoder")
        self.geometry("400x400")

        self.label = tk.Label(self, text="Input Text or Select Image File")
        self.label.pack(pady=10)

        self.text_input = tk.Text(self, height=4)
        self.text_input.pack(pady=10)

        self.encode_button = tk.Button(self, text="Encode Text", command=self.encode_text)
        self.encode_button.pack(pady=5)

        self.decode_button = tk.Button(self, text="Decode Text", command=self.decode_text)
        self.decode_button.pack(pady=5)
        
        self.file_button = tk.Button(self, text="Select Image File", command=self.select_file)
        self.file_button.pack(pady=5)

        self.result_label = tk.Label(self, text="Result")
        self.result_label.pack(pady=10)

        self.result_text = tk.Text(self, height=8)
        self.result_text.pack(pady=10)

    def encode_text(self):
        message = self.text_input.get("1.0", tk.END).strip()
        if message:
            b64 = base64(message, 'string')
            encoded_output = b64.encode()
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", encoded_output)
        else:
            messagebox.showwarning("Input Error", "Please enter text to encode")

    def decode_text(self):
        encoded_message = self.text_input.get("1.0", tk.END).strip()
        if encoded_message:
            try:
                b64 = base64(encoded_message, 'string')
                decoded_output = b64.decode(encoded_message)
                self.result_text.delete("1.0", tk.END)
                self.result_text.insert("1.0", decoded_output)
            except Exception as e:
                messagebox.showerror("Decode Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please enter encoded text to decode")

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            b64_image = base64(file_path, 'image')
            encoded_image = b64_image.encode()
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", encoded_image)
            decode_prompt = messagebox.askyesno("Decode Image", "Do you want to decode the image now?")
            if decode_prompt:
                b64_image.decode(encoded_image)
        else:
            messagebox.showwarning("File Selection Error", "Please select a valid image file")

if __name__ == "__main__":
    app = Base64EncoderGUI()
    app.mainloop()
