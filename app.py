from flask import Flask, render_template, request
from docx import Document

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return "No se ha subido ningún archivo", 400

    file = request.files['file']
    doc = Document(file)

    # Variables para el análisis
    font_issues = 0
    justification_issues = 0
    word_count = 0

    # Análisis de palabras y formato
    for paragraph in doc.paragraphs:
        word_count += len(paragraph.text.split())

        # Verificar fuente y tamaño
        if paragraph.style.font.name != "Arial" or (paragraph.style.font.size and paragraph.style.font.size.pt != 11):
            font_issues += 1

        # Verificar justificación
        if paragraph.alignment not in [3, None]:  # 3 es justificado
            justification_issues += 1

    # Pasar resultados al HTML
    results = {
        "font_issues": font_issues,
        "justification_issues": justification_issues,
        "word_count": word_count
    }
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
