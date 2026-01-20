import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image
import os

def select_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")])
    if file_path:
        video_entry.delete(0, tk.END)
        video_entry.insert(0, file_path)

def generate_pdf():
    video_path = video_entry.get()
    if not video_path:
        messagebox.showerror("Error", "Please select a video file")
        return
    try:
        frames_por_segundo = int(fps_entry.get())
        if frames_por_segundo <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid FPS value. Must be a positive integer")
        return
    
    output_pdf = "PDF/output.pdf"
    
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            messagebox.showerror("Error", "Could not open video file")
            return
        
        fps_original = cap.get(cv2.CAP_PROP_FPS)
        if fps_original == 0:
            messagebox.showerror("Error", "Could not get video FPS")
            return
        
        intervalo = int(fps_original / frames_por_segundo)
        if intervalo == 0:
            intervalo = 1  # Minimum interval
        
        frames = []
        frame_count = 0
        saved = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            if frame_count % intervalo == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                frames.append(img)
                saved += 1
            
            frame_count += 1
        
        cap.release()
        
        if frames:
            frames[0].save(
                output_pdf,
                save_all=True,
                append_images=frames[1:]
            )
            messagebox.showinfo("Success", f"PDF generated with {saved} frames")
            # Open the folder containing the PDF
            os.startfile(os.path.dirname(os.path.abspath(output_pdf)))
        else:
            messagebox.showerror("Error", "No frames were extracted from the video")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Video to PDF Converter")

tk.Label(root, text="Video File:").grid(row=0, column=0, padx=10, pady=10)
video_entry = tk.Entry(root, width=50)
video_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_video).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Frames per second:").grid(row=1, column=0, padx=10, pady=10)
fps_entry = tk.Entry(root)
fps_entry.insert(0, "2")
fps_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Generate PDF", command=generate_pdf).grid(row=2, column=1, pady=20)

root.mainloop()