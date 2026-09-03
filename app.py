import gradio as gr
from tracker import TrafficAnalyzer
import os

# Initialize the tracking engine
analyzer = TrafficAnalyzer('yolov8n.pt')


def analyze_traffic(video_file):
	if video_file is None:
		return None, "Error: Please upload a video."

	# Define where to save the processed video
	output_path = "output_tracked.mp4"

	# Run the computer vision engine
	processed_vid, count = analyzer.process_video(video_file, output_path)

	return processed_vid, f"✅ Analysis Complete! Total unique vehicles tracked: {count}"


# Build the UI
with gr.Blocks(title="Smart City Traffic Analyzer", theme=gr.themes.Base()) as demo:
	gr.Markdown("# 🚦 Smart Traffic Tracker")
	gr.Markdown(
		"Upload a dashcam or highway traffic video. The system uses **YOLOv8** and **ByteTrack** to identify vehicles, maintain their IDs across frames, and count them as they cross a virtual tripwire.")

	with gr.Row():
		with gr.Column():
			video_input = gr.Video(label="Upload Traffic Video (MP4/AVI)")
			analyze_btn = gr.Button("Analyze Traffic Flow", variant="primary")

		with gr.Column():
			video_output = gr.Video(label="Tracked Output Video")
			stats_output = gr.Textbox(label="Analytics Results")

	analyze_btn.click(fn=analyze_traffic, inputs=video_input, outputs=[video_output, stats_output])

if __name__ == "__main__":
	# Port 7860 is required for free Hugging Face Spaces deployment
	demo.launch(server_name="0.0.0.0", server_port=7860, share=True)