# 🚀 URL Shortener  
[![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-blue.svg)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


![URL Shortener Demo](https://your-image-link-here.com/demo.gif)

# 📌 URL Shortener  
A simple and efficient URL shortener built with Flask, SQLite, and Bootstrap.

## 🚀 Features  
✅ Shorten long URLs  
✅ Copy shortened links with one click  
✅ 🔄 Refresh button to reset input  
✅ 💾 Uses SQLite for storage  
✅ 🎨 Clean and responsive UI  

## 🛠️ Installation  

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/doona1/URL-Shortner.git
   cd URL-Shortner


## 🔍 How It Works  
1️⃣ **User enters a long URL**  
2️⃣ **The app generates a unique short code**  
3️⃣ **Stores it in the SQLite database**  
4️⃣ **Redirects users to the original URL when they visit the short link**  

### ✨ Example Code
```python
@app.route("/<short_code>")
def redirect_short_url(short_code):
    long_url = shortened_urls.get(short_code)
    if long_url:
        return redirect(long_url)
    return "URL not found", 404



---

## **7️⃣ Add Contact & Support Section**
Include links to your **GitHub, LinkedIn, or Portfolio**.

### **Example:**
```md
## 💬 Contact  
📧 Email: your-email@example.com  
🐦 Twitter: [@yourhandle](https://twitter.com/yourhandle)  
👨‍💻 LinkedIn: [Your Name](https://www.linkedin.com/in/yourname/)  
📂 GitHub: [doona1](https://github.com/doona1)


## 🔮 Upcoming Features  
- ✅ Custom short links (e.g., mysite.com/customname)  
- ✅ QR code generation for shortened links  
- ✅ Click tracking & analytics  

## 🔮 Upcoming Features  
- ✅ Custom short links (e.g., mysite.com/customname)  
- ✅ QR code generation for shortened links  
- ✅ Click tracking & analytics  

[![Issues](https://img.shields.io/github/issues/doona1/URL-Shortner)](https://github.com/doona1/URL-Shortner/issues)
[![Stars](https://img.shields.io/github/stars/doona1/URL-Shortner)](https://github.com/doona1/URL-Shortner/stargazers)
[![Forks](https://img.shields.io/github/forks/doona1/URL-Shortner)](https://github.com/doona1/URL-Shortner/network/members)
