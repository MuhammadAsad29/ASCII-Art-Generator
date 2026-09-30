import os
from flask import Flask, request, jsonify, render_template
from ascii_engine import image_to_ascii

app = Flask(__name__)
# Max upload size: 16MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files['image']
    if not file.filename:
        return jsonify({"error": "Empty filename"}), 400

    try:
        # Parse parameters with safe defaults
        width = int(request.form.get('width', 100))
        width = max(20, min(width, 250))  # Clamp between 20 and 250 for web display
        
        style = request.form.get('style', 'standard')
        invert = request.form.get('invert', 'false').lower() == 'true'
        color_mode = request.form.get('color_mode', 'false').lower() == 'true'
        contrast = float(request.form.get('contrast', 1.0))
        contrast = max(0.5, min(contrast, 2.5))

        file_bytes = file.read()
        result = image_to_ascii(
            file_bytes=file_bytes,
            target_width=width,
            style=style,
            invert=invert,
            contrast=contrast,
            color_mode=color_mode
        )
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
