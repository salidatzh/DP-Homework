# Rod Cutting Problemi (Dinamik Programlama)

Bu proje, Rod Cutting (Çubuk Kesme) problemini **Dinamik Programlama (DP)** yaklaşımıyla çözmektedir.

---
## 🧩 Problem Tanımı
Uzunluğu `n` olan bir çubuk, farklı uzunluklarda kesilerek satılabilir. Amaç, kesimleri öyle yapmak ki toplam kazanç maksimum olsun.

---
## 🧠 Dinamik Programlama Nedir?
Problemi alt problemlere bölüp, bu alt problemlerin sonuçlarını tekrar kullanarak çözme yöntemidir.

---
## 💡 Kullanılan Yaklaşım
- **Recurrence Relation:**
  R(n) = max( price[i-1] + R(n - i) ), 1 ≤ i ≤ n  
- **Base Case:** R(0) = 0
  
---
## 💻 Kod Dili
Python

---
## 🧠 Karmaşıklık
- Zaman: O(n²)  
- Bellek: O(n)

---
## 👩‍🎓 Yazar
**Salidat Cakıpbekova 2204.01016**  
Algoritma Uygulamaları (BİL-377) – Abdulkadir Şeker  
Teslim Tarihi: 11.11.2025
