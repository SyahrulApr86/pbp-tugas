# Tugas 6: Javascript dan AJAX

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester
Ganjil 2022/2023

## Nama: Syahrul Apriansyah

## NPM : 2106708311

## link deploy: https://tugas-pbp-syahrul.herokuapp.com/todolist/

###  Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_!

<b>Penjelasan:</b>

Asynchronous programming melakukan pekerjaannya tanpa harus terikat dengan proses lain atau dapat kita sebut secara Independent. Sedangkan Synchronous programming melakukan pekerjaannya secara berurutan atau harus menunggu proses sebelumnya selesai terlebih dahulu.

###  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma _Event-Driven Programming_. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

<b>Penjelasan:</b>

Event-Driven Programming adalah paradigma pemrograman yang berfokus pada event. Event adalah sebuah kejadian yang terjadi pada suatu objek. Contoh penerapannya pada tugas ini adalah ketika kita menekan tombol submit, maka akan terjadi sebuah event yang akan memanggil fungsi yang telah kita buat.

Contoh penerapan event-driven programming pada tugas ini adalah pada penggunaan method AJAX POST untuk menambahkan tasks. Function JavaScript createTask() saya buat untuk menggunakan method POST. Function ini menerima var berupa data task, di mana data tersebut diambil dari submisi form. Form yang dimaksud adalah form yang melalui modal memiliki button submit dengan tag ` onclick="createTask()" `, artinya function createTask() dijalankan ketika button tersebut ditekan.  

###  Jelaskan penerapan _asynchronous programming_ pada AJAX.

<b>Penjelasan:</b>

Yang berarti bahwa browser tidak perlu memuat ulang seluruh halaman ketika hanya sedikit data pada halaman yang berubah. AJAX hanya meneruskan informasi yang diperbarui ke dan dari server.

###   Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas.

<b>Penjelasan:</b>

1) Membuat view show_json yang mengembalikan data task user dalam bentuk JSON.
2) Membuat routing path /todolist/json yang mengarah ke view tersebut.
3) Membuat JS function yang bernama handleCards() untuk mengambil dan merender cards dari database JSON melalui method GET yang diarahkan ke halaman todolist/json/.
4) Menampilkan halaman utama todolist yang telah merender task cards melalui function (document).ready
5) Membuat view todolist_ajax, kemudian membuat routing path todolist/add/ yang mengarah ke view tersebut.
6) Membuat modal Bootstrap dengan form untuk menambahkan task.
7) Membuat JS function bersama createTask() yang melalui method POST mengambil data input dengan type submit dari form pembuatan task. Data tersebutkan diarahkan ke todolist/add/, memanggil fungsi todolist_ajax yang ada pada views.py, dan menampilkan response secara asinkronus tanpa reload page.

