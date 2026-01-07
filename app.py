from flask import Flask, request, jsonify
from flask_cors import CORS
import difflib

app = Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    return "Server Chatbot Berjalan! Silakan buka index.html untuk chat."

# Database sederhana
knowledge_base = {
    "halo": "Halo saya adalah Zheaww Asisten Virtual Agyl Wendi Pratama! Senang bertemu denganmu.",
    "hai": "Halo saya adalah Zheaww Asisten Virtual Agyl Wendi Pratama! Senang bertemu denganmu.",
    "hi": "Halo saya adalah Zheaww Asisten Virtual Agyl Wendi Pratama! Senang bertemu denganmu.",
    
    "nama": "Nama saya Agyl Wendi Pratama, biasa dipanggil Agyl atau Wendi hehe.",
    "siapa kamu": "Saya adalah seorang Web Developer dan AI Enthusiast.",
    "tanggal lahir": "Saya lahir pada tanggal 11 September 2005.",
    "alamat": "Saya tinggal di Kota Bengkulu, Provinsi Bengkulu, Indonesia.",
    "umur": "Coba hitung sendiri ya hehe saya lahir tahun 2005.",
    "usia": "Coba hitung sendiri ya hehe saya lahir tahun 2005.",
    "asal": "Saya berasal dari Kota Pagar Alam, Provinsi Sumatera Selatan, Indonesia.",
    "tempat lahir": "Saya lahir di Kota Pagar Alam, Provinsi Sumatera Selatan, Indonesia.",
    
    "kuliah": "Saya kuliah di Universitas Bengkulu, jurusan Teknik Informatika.",
    "kampus": "Saya kuliah di Universitas Bengkulu (UNIB).",
    "sekolah": "Riwayat pendidikan saya meliputi SD Muhammadiyah 1 Kota Pagar Alam, SMP Negeri 1 Kota Pagar Alam, SMA Negeri 1 Kota Pagar Alam, dan sekarang sedang menempuh pendidikan di Universitas Bengkulu.",
        
    "hobi": " Pada waktu luang saya senang mencari hal baru yang berhubungan dengan teknologi dan juga luar angkasa, saya juga suka bermain game dan juga menonton film.",
    "skill": "Saya memiliki keahlian dalam pengembangan web (Frontend dan Backend), dan Python programming.",
    "bisa apa": "Saya dapat menggunakan berbagai bahasa pemrograman seperti Python, JavaScript, dan HTML/CSS. Saya juga tertarik dengan pengembangan web dan kecerdasan buatan.",
    "makanan favorit": "Saya suka mie ayam dan nasi goreng.",
    "minuman favorit": "Saya suka berbagai jenis olahan minuman matcha.",
    
    "kontak": "Kamu bisa menghubngi saya melalui email, atau DM saya di Instagram.",
    "email": "Kamu bisa menghubungi saya melalui email di agylwendipratama09@gmail.com",
    "instagram": "Kamu bisa follow Instagram saya di @agylwendipratama",
    "ig": "Kamu bisa follow Instagram saya di @agylwendipratama",
    "github": "Kamu bisa cek project saya di GitHub: https://github.com/likeazwee (likeazwee)",
    "linkedin": "Kamu bisa terhubung dengan saya di LinkedIn: https://www.linkedin.com/in/agylwndiprtma11/",
    "Discord": "Kamu bisa add Discord saya di Zweendq#3629",
    
    "pacar": "hehe itu privasi gasi, silahkan tanya pertanyaan lainnya hehe.",
    "ganteng": "Makasih hehe, kamu juga ganteng/cantik kok!",
    
    "terima kasih": "Sama-sama! Senang bisa mengobrol bersamamu.",
    "terimakasih": "Sama-sama! Senang bisa mengobrol bersamamu.",
    "thanks": "Sama-sama! Senang bisa mengobrol bersamamu.",
    "thank you": "Sama-sama! Senang bisa mengobrol bersamamu.",
    "bye": "Sampai jumpa lagi! Semoga harimu menyenangkan.",
    "dadah": "Dadah! Sampai Jumpa Lagi.",
    
}

def get_bot_response(text):
    text = text.lower()
    
    for key in knowledge_base:
        if key in text:
            return knowledge_base[key]
            
    matches = difflib.get_close_matches(text, knowledge_base.keys(), n=1, cutoff=0.6)
    if matches:
        return knowledge_base[matches[0]]
        
    return "Maaf, saya tidak mengerti. Coba kata lain."

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    bot_reply = get_bot_response(user_message)

    return jsonify({
        "reply": bot_reply,
        "status": "success"
    })
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)