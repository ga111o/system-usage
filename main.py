from flask import Flask, jsonify, render_template
import psutil
import GPUtil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usage')
def system_usage():
    # CPU 사용량
    cpu_usage = psutil.cpu_percent(interval=1)

    # RAM 사용량
    memory_info = psutil.virtual_memory()
    ram_usage = memory_info.percent

    # GPU 사용량
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]
        gpu_usage = gpu.load * 100
        vram_usage = gpu.memoryUtil * 100
    else:
        gpu_usage = None
        vram_usage = None

    return jsonify({
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'gpu_usage': gpu_usage,
        'vram_usage': vram_usage
    })

if __name__ == '__main__':
    app.run(debug=True)
