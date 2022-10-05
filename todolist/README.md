# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester
Ganjil 2022/2023

## Nama: Syahrul Apriansyah

## NPM : 2106708311

## link deploy: https://tugas-pbp-syahrul.herokuapp.com/todolist/

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing _style_?

<b>Penjelasan:</b>

Inline CSS adalah cara untuk menambahkan style ke elemen HTML. Inline CSS menggunakan atribut style pada elemen HTML. Inline CSS tidak disarankan karena tidak dapat digunakan untuk memisahkan style dari konten, dan tidak dapat digunakan untuk mengulang style yang sama untuk beberapa elemen.

Internal CSS adalah cara untuk menambahkan style ke elemen HTML. Internal CSS menggunakan tag style di dalam bagian head dokumen HTML. Internal CSS dapat digunakan untuk memisahkan style dari konten, dan dapat digunakan untuk mengulang style yang sama untuk beberapa elemen.

External CSS adalah cara untuk menambahkan style ke elemen HTML. External CSS menggunakan tag link untuk merujuk ke file CSS eksternal. External CSS dapat digunakan untuk memisahkan style dari konten, dan dapat digunakan untuk mengulang style yang sama untuk beberapa elemen.

###  Jelaskan tag HTML5 yang kamu ketahui.

<b>Penjelasan:</b>

Tag HTML5 yang saya ketahui adalah:
<ul>
<li>p tag untuk membuat paragraf</li>
<li>h1 tag untuk membuat heading</li>
<li>a tag untuk membuat hyperlink</li>
<li>img tag untuk menambahkan gambar</li>
<li>table tag untuk membuat tabel</li>
<li>form tag untuk membuat form</li>
<li>input tag untuk membuat input</li>
<li>button tag untuk membuat tombol</li>
<li>div tag untuk membuat divisi</li>
<li>span tag untuk membuat span</li>
<li>ul tag untuk membuat list</li>
<li>ol tag untuk membuat list</li>
<li>li tag untuk membuat list</li>
</ul>

### Jelaskan tipe-tipe CSS selector yang kamu ketahui.

<b>Penjelasan:</b>

<ul>
<li>Universal Selector: Berfungsi untuk memilih semua elemen pada halaman web.</li>
<li>Element Selector: Berfungsi untuk memilih elemen tertentu pada halaman web.</li>
<li>Class Selector: Berfungsi untuk memilih elemen yang memiliki class tertentu pada halaman web.</li>
<li>ID Selector: Berfungsi untuk memilih elemen yang memiliki id tertentu pada halaman web.</li>
<li>Grouping Selector: Berfungsi untuk memilih beberapa elemen pada halaman web.</li>
<li>Descendant Selector: Berfungsi untuk memilih elemen yang merupakan turunan dari elemen lain pada halaman web.</li>
<li>Child Selector: Berfungsi untuk memilih elemen yang merupakan anak dari elemen lain pada halaman web.</li>
<li>Adjacent Sibling Selector: Berfungsi untuk memilih elemen yang merupakan saudara kembar dari elemen lain pada halaman web.</li>
<li>General Sibling Selector: Berfungsi untuk memilih elemen yang merupakan saudara dari elemen lain pada halaman web.</li>
<li>Attribute Selector: Berfungsi untuk memilih elemen yang memiliki atribut tertentu pada halaman web.</li>
<li>Pseudo-class Selector: Berfungsi untuk memilih elemen yang memiliki pseudo-class tertentu pada halaman web.</li>
<li>Pseudo-element Selector: Berfungsi untuk memilih elemen yang memiliki pseudo-element tertentu pada halaman web.</li>
</ul>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

<b>Penjelasan:</b>

1. Mendefinisikan link src bootstrap ke dalam tag `<head>`
2. Membuat struktur HTML dengan menggunakan class dan menyesuaikan bootstrap sesuai kebutuhan, untuk membuat cards pada todolist menggunakan `class="card"`
3. Mengubah style dari tampilan bootstrap dengan menambahkan Internal CSS ke dalam tag `<style>`
4. Push ke github untuk deploy ke heroku

# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

###  Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen` <form>`?

<b>Penjelasan:</b>

 Token ini juga digunakan untuk menghindari serangan CSRF (Cross Site Request Forgery). CSRF adalah serangan yang memanfaatkan kepercayaan antara browser dan server. CSRF mengharuskan browser untuk mengirimkan permintaan yang tidak diinginkan ke server. CSRF dapat dilakukan dengan cara mengirimkan permintaan melalui email, chat, atau situs web yang terinfeksi. CSRF dapat mengakibatkan kerusakan pada data, penghapusan data, dan penyalahgunaan hak akses.
 
#### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

<b>Penjelasan:</b>

Dengan membuat elemen form secara manual, kita dapat mengatur tampilan form sesuai dengan keinginan kita. Cara membuat form secara manual adalah dengan menambahkan elemen form seperti input, textarea, select, dan lain-lain. Kemudian kita dapat mengatur tampilan form tersebut dengan menambahkan class, id, dan lain-lain.

#### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada _template_ HTML.

<b>Penjelasan:</b>

Ketika user menambahkan task baru pada form dibuat, task tersebut akan tersimpan pada database sebagai objek dari model task untuk ditampilkan pada HTML . Kita perlu mengambil objek dari task yang difilter berdasarkan user yang sedang login dan direturn dalam bentuk dictionary sehingga dapat diakses dalam HTML.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

<b>Penjelasan:</b>

Pertama kita membuatapp todolist yang kemudian kita registrasi di `project_django` yang menginisiasi class Task yang ada di `models.py`, data tersebut berisi dari user, data, date, dan deskripsi, ketiga hal tersebut yang memberikan apa saja data yang akan kita gunakan selanjutnya


