 Django Alışveriş Sitem

Bu proje, Python ve Django framework'ü kullanılarak geliştirilmiş tam özellikli bir e-ticaret web sitesidir. Kullanıcılar, ürünlere göz atabilir, sepetlerine ekleyebilir, sipariş verebilir ve sipariş geçmişlerini görüntüleyebilirler. Proje, güvenli bir kullanıcı deneyimi sunmak için tasarlanmıştır.

Özellikler

Ürünleri kategoriye göre filtreleme ve fiyata göre sıralama.

Kullanıcı kaydı, girişi ve çıkışı.

Ürünleri sepete ekleme, miktarı güncelleme ve silme.

Ödeme ve sipariş onayı.

Kullanıcıya özel sipariş geçmişi ve profil sayfası.

Django'nun yerleşik yönetici paneli ile ürün, kategori, sipariş ve kullanıcı yönetimi.

Ekran Görüntüleri

Projenin temel görünümleri aşağıdadır.

### Web Sitesi

**Ürün Sayfası (Filtreleme ve Sıralama)**

![Ürün Sayfası](https://github.com/Rubinaerin/django-alisveris-sitem/blob/main/Ekran%20Resmi%202025-09-01%2017.19.41.png)![Ürün Sayfası](https://github.com/Rubinaerin/django-alisveris-sitem/blob/main/Ekran%20Resmi%202025-09-01%2017.19.24.png)

**Sepet ve Sipariş Onayı**

![Sepet ve Ödeme](https://github.com/Rubinaerin/django-alisveris-sitem/blob/main/Ekran%20Resmi%202025-09-01%2017.21.14.png)![Sepet ve Ödeme](https://github.com/Rubinaerin/django-alisveris-sitem/blob/main/Ekran%20Resmi%202025-09-01%2017.21.00.png)

**Profil ve Sipariş Geçmişi**

![Profilim](https://github.com/Rubinaerin/django-alisveris-sitem/blob/main/Ekran%20Resmi%202025-09-01%2017.22.22.png)

**Kayıt ve Giriş Sayfaları**

![Giriş Yap](https://github.com/Rubinaerin/django-alisveris-sitem/blob/main/Ekran%20Resmi%202025-09-01%2017.18.55.png)

### Django Yönetici Paneli

**Yönetici Paneli Genel Görünüm**

![Admin Paneli](https://github.com/Rubinaerin/django-alisveris-sitem/blob/main/Ekran%20Resmi%202025-09-01%2017.26.51.png)

**Kullanıcı Yönetimi**

![Kullanıcılar](https://github.com/Rubinaerin/django-alisveris-sitem/blob/main/Ekran%20Resmi%202025-09-01%2017.28.12.png)

Kurulum

Projenizi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Depoyu klonlayın:

git clone https://github.com/Rubinaerin/django-alisveris-sitem.git
cd django-alisveris-sitem
2. Sanal ortamı oluşturun ve etkinleştirin:

python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate    # Windows
3. Gerekli paketleri kurun:

pip install -r requirements.txt
pip install python-dotenv
Not: Projenizde requirements.txt dosyası yoksa, kurulu paketleri oluşturmak için pip freeze > requirements.txt komutunu kullanın.

4. .envdosyasını oluşturun veSECRET_KEY'i ekleyin.
Projenizin ana dizininde .env adlı bir dosya oluşturun ve içine aşağıdakini ekleyin:

SECRET_KEY=yeni-bir-secret-key-buraya
Not: django-insecure- ile başlayan eski anahtarınızı buraya yapıştırabilirsiniz, ancak güvenlik için yeni bir anahtar oluşturmanız önerilir.

5. Veritabanı geçişlerini (migrations) çalıştırın:

python manage.py makemigrations
python manage.py migrate
6. Süper kullanıcı oluşturun (admin paneline erişmek için):

python manage.py createsuperuser
7. Sunucuyu başlatın:

python manage.py runserver
8. Tarayıcınızda http://127.0.0.1:8000/ adresine giderek siteyi görüntüleyin.
