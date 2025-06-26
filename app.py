import os
import socket
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)
BASE_DIR = os.path.abspath(".")

UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list_images", methods=['POST'])
def list_images():
    folder = request.json.get('folder')
    abs_folder = os.path.abspath(folder)
    # 간단 보안: BASE_DIR 하위만 허용
    if not abs_folder.startswith(BASE_DIR):
        return jsonify({'error': 'Invalid folder'}), 400

    files = []
    for fname in os.listdir(abs_folder):
        if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
            files.append(os.path.join(folder, fname).replace("\\", "/"))
    return jsonify({'images': files})

@app.route("/upload", methods=['POST'])
def upload():
    img_file = request.files['file']
    img_path = os.path.join(UPLOAD_FOLDER, img_file.filename)
    img_file.save(img_path)
    return jsonify({'url': f"/static/uploads/{img_file.filename}"})

# 폴더 탐색용(선택 UI용)
@app.route("/list_dirs", methods=['GET'])
def list_dirs():
    parent = request.args.get('parent', BASE_DIR)
    parent = os.path.abspath(parent)
    if not parent.startswith(BASE_DIR):
        return jsonify({'error': 'Invalid parent'}), 400
    dirs = []
    for name in os.listdir(parent):
        path = os.path.join(parent, name)
        if os.path.isdir(path):
            dirs.append({'name': name, 'path': path.replace("\\", "/")})
    return jsonify({'dirs': dirs})

def find_free_port(start=5000, end=15000):
    for port in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('localhost', port))
                return port
            except OSError:
                continue
    raise RuntimeError("사용 가능한 포트가 없습니다.")

if __name__ == "__main__":
    port = find_free_port(6000, 10000)
    print(f"\n\n>>> 서버를 {port} 포트에 엽니다. 브라우저에서 http://localhost:{port} 접속하세요.\n")
    app.run(debug=True, port=port, host="0.0.0.0")