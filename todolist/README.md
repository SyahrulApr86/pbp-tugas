# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester
Ganjil 2022/2023

## Nama: Syahrul Apriansyah

## NPM : 2106708311

## link deploy: https://tugas-pbp-syahrul.herokuapp.com/todolist/


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


