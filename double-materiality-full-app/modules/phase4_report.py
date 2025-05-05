from flask import Blueprint, render_template, request, send_file
from reportlab.pdfgen import canvas
from openpyxl import Workbook
import io, os
from datetime import datetime

bp = Blueprint('phase4', __name__, template_folder='../templates')

@bp.route('/', methods=['GET'])
def summary():
    return render_template('phase4_report.html')

@bp.route('/generate', methods=['POST'])
def generate():
    fmt = request.form.get('format')
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    if fmt=='pdf':
        buf = io.BytesIO()
        c = canvas.Canvas(buf)
        c.drawString(100,800,"Sustainability Report")
        c.save()
        buf.seek(0)
        return send_file(buf, attachment_filename=f'report_{now}.pdf', as_attachment=True)
    else:
        wb = Workbook()
        ws = wb.active
        ws.title="Report"
        path = f"reports/report_{now}.xlsx"
        wb.save(path)
        return send_file(path, as_attachment=True)
