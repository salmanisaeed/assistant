
from flask import Flask, request, jsonify

app = Flask(__name__)

# متن کامل کتاب
book_content = """
فراتر از لوگو
ساختار و استراتژی‌های برندسازی مدرن
مولف : سعید سلمانی زادگان
این کتاب را با عشق تقدیم می‌کنم به همسر مهربانم که همواره پشتیبان من بوده و دو دختر عزیزم که با حضورشان به زندگی‌ام نور و معنا بخشیدند.

فهرست:
پیش‌گفتار…………………………………………………….1
مقدمه………………………………………………………..3

فصل اول: مفهوم برند و اهمیت آن در دنیای مدرن
1.1 مقدمه
1.2 تعریف برند
1.3 تاریخچه برند
1.4 اهمیت برند در بازارهای رقابتی
1.5 تأثیر برند بر رفتار مصرف‌کننده
1.6 تأثیر اجتماعی برند
1.7 استراتژی‌های برندینگ
1.8 موقعیت‌یابی برند
1.9 طراحی هویت برند
1.10 فناوری و برند
1.11 نتیجه‌گیری

... (ادامه متن کتاب)
"""

# خلاصه نمونه برای کل کتاب
book_summary = """
این کتاب به بررسی ساختار و استراتژی‌های برندسازی مدرن می‌پردازد و اهمیت برند در بازارهای رقابتی، تأثیر اجتماعی و رفتار مصرف‌کننده را مورد تحلیل قرار می‌دهد.
"""

# جستجو در کتاب
@app.route("/search", methods=["GET"])
def search_book():
    query = request.args.get("query", "").lower()
    if not query:
        return jsonify({"error": "لطفاً یک عبارت جستجو وارد کنید."}), 400

    results = [line for line in book_content.split("\n") if query in line.lower()]
    if results:
        return jsonify({"results": results[:5]})
    else:
        return jsonify({"message": "متن مرتبطی یافت نشد."})

# خلاصه کتاب
@app.route("/summary", methods=["GET"])
def get_summary():
    return jsonify({"summary": book_summary})

# دسترسی به فصل‌های کتاب
@app.route("/chapter", methods=["GET"])
def get_chapter():
    chapter_number = request.args.get("number")
    if not chapter_number or not chapter_number.isdigit():
        return jsonify({"error": "لطفاً شماره فصل را وارد کنید."}), 400

    chapter_key = f"فصل {chapter_number}"
    chapters = [line for line in book_content.split("\n") if chapter_key in line]
    if chapters:
        return jsonify({"chapter": chapters})
    else:
        return jsonify({"message": f"فصل {chapter_number} یافت نشد."})

if __name__ == "__main__":
    app.run(debug=True)
