from flask import Flask, render_template, request
import json

app = Flask(__name__)

def load_videos():
    with open('videos.json') as f:
        return json.load(f)

@app.route('/')
def index():
    videos = load_videos()
    query = request.args.get('q', '').lower()
    if query:
        videos = [video for video in videos if query in video['title'].lower()]
    return render_template('index.html', videos=videos)

@app.route('/watch/<int:video_id>')
def watch(video_id):
    videos = load_videos()
    if 0 <= video_id < len(videos):
        return render_template('watch.html', video=videos[video_id], video_id=video_id)
    return "Video not found", 404

if __name__ == '__main__':
    app.run(debug=True)
