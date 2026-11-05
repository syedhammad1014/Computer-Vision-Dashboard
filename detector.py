import numpy as np
from PIL import Image, ImageDraw, ImageFont

class ObjectDetector:
    def __init__(self):
        self.classes = ["Person", "Car", "Laptop", "Smartphone", "Book", "Chair"]
        self.colors = ["#00F0FF", "#7000FF", "#00FF88", "#FF0055", "#FF9900", "#FFD700"]

    def detect(self, pil_image, conf_threshold=0.5):
        img_copy = pil_image.copy()
        draw = ImageDraw.Draw(img_copy)
        w, h = pil_image.size
        
        # Simulated robust detection output
        detections = []
        sample_boxes = [
            (int(w * 0.15), int(h * 0.2), int(w * 0.45), int(h * 0.8), "Person", 0.94),
            (int(w * 0.55), int(h * 0.45), int(w * 0.85), int(h * 0.75), "Laptop", 0.88),
        ]
        
        for idx, (x1, y1, x2, y2, label, score) in enumerate(sample_boxes):
            if score >= conf_threshold:
                color = self.colors[idx % len(self.colors)]
                draw.rectangle([x1, y1, x2, y2], outline=color, width=4)
                draw.rectangle([x1, y1 - 22, x1 + 120, y1], fill=color)
                draw.text((x1 + 6, y1 - 20), f"{label} {int(score * 100)}%", fill="#000000")
                detections.append({
                    "Object": label,
                    "Confidence": f"{score * 100:.1f}%",
                    "Bounding Box (X1, Y1, X2, Y2)": f"({x1}, {y1}, {x2}, {y2})"
                })
                
        return img_copy, detections
