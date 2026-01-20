import cv2
from PIL import Image
import os

video_path = "D:/Py/Video para PDF/Video/Joelma.mp4"
frames_por_segundo = 2
output_pdf = "D:/Py/Video para PDF/PDF/output.pdf"

cap = cv2.VideoCapture(video_path)

fps_original = cap.get(cv2.CAP_PROP_FPS)
intervalo = int(fps_original / frames_por_segundo)

frames = []
frame_count = 0
saved = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % intervalo == 0:
        # OpenCV usa BGR, Pillow usa RGB
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

print(f"PDF gerado com {saved} frames")
