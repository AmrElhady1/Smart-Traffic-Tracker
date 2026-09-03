import cv2
import numpy as np
from ultralytics import YOLO


class TrafficAnalyzer:
	def __init__(self, model_path='yolov8n.pt'):
		# Auto-downloads the nano model if it doesn't exist locally
		self.model = YOLO(model_path)

	def process_video(self, video_path, output_path):
		cap = cv2.VideoCapture(video_path)

		# Get video properties
		width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		fps = int(cap.get(cv2.CAP_PROP_FPS))

		# Setup video writer (mp4 format)
		fourcc = cv2.VideoWriter_fourcc(*'mp4v')
		out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

		# Define a virtual counting line across the middle of the frame
		line_y = height // 2
		crossed_ids = set()  # Store IDs of vehicles that crossed

		while cap.isOpened():
			success, frame = cap.read()
			if not success:
				break

			# Run YOLO detection + tracking
			# classes=[2, 3, 5, 7] filters for cars, motorcycles, buses, and trucks
			results = self.model.track(frame, persist=True, classes=[2, 3, 5, 7], verbose=False)

			# Check if any objects are detected and tracked
			if results[0].boxes is not None and results[0].boxes.id is not None:
				boxes = results[0].boxes.xyxy.cpu().numpy()
				track_ids = results[0].boxes.id.int().cpu().tolist()

				for box, track_id in zip(boxes, track_ids):
					x1, y1, x2, y2 = map(int, box)
					cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Calculate center of the vehicle

					# Draw bounding box and center dot
					cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
					cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
					cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10),
								cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

					# Detection logic: if the center of the car crosses the virtual line
					if line_y - 15 < cy < line_y + 15:
						crossed_ids.add(track_id)

			# Draw the virtual tripwire & display the live count
			cv2.line(frame, (0, line_y), (width, line_y), (255, 0, 0), 2)
			cv2.putText(frame, f"Total Vehicles: {len(crossed_ids)}", (50, 50),
						cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

			out.write(frame)

		cap.release()
		out.release()
		return output_path, len(crossed_ids)