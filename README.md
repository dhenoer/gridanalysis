# GRID ANALISYS

![Screenshot](img/grid-analisys.png)

Grid-Analisys ini adalah program berbasis text sebagai 
alat bantu untuk Decision Support System. Berguna untuk menentukan
pilihan berdasarkan skor dengan mempertimbangkan bobot dan skor faktor.

## Cara Pakai

Cara pakai sbb:

### Topik

Input topik yang ingin dipecahkan masalahnya. Misal:
* Kapan saya harus pulang?
* Mobil apa yang harus saya beli?
* Pasangan Capres mana yang mau saya pilih?
dll

### Pilihan

Input pilihan yang akan ditentukan atas topik di atas. Input satu baris disahkan dengan koma. Misal
* Besok, Lusa
* Citycar, Sedan, Minibus
* Jokowi-Maruf, Prabowo-Sandi
dll

### Faktor

Input faktor-faktor apa yang perlu dipertimbangkan untuk memilih pilihan tsb. Diinput satu baris dipisah koma. Misal:
* Lelah, Kangen, Wisata Kuliner
* Harga, Hemat, Airbag, Harga Jual, After Service
* Pengalaman, VisiMisi, Cerdas, Berani, Jujur
dll

### Bobot

Input besarnya bobot dari setiap faktor. Bobot ini akan memberikan 
faktor mana yang lebih penting / berharga dibanding yang lain. 
Kalau semua angka sama, berarti tidak ada yang dipentingkan. Diinput satu baris dipisah koma. Misal:
* 3, 4, 2
* 2, 2, 2, 1, 3
* 1, 2, 1, 2, 2
dll
 
### Skor 

Input skor dalam skala 1-5 untuk memilih suatu pilihan berdasarkan faktor-faktor tertentu. Skor ini menggambarkan perbandingan kecenderungan memilih pilihan berdasarkan suatu faktor.

Misal:
Mempertimbangkan faktor 'Lelah', user memberi skor
* 3 untuk pilihan 'Pulang Besok'
* 4 untuk pilihan 'Pulang Lusa'

Sementara dgn mempertimbangkan faktor 'Kagen', user memberi skor
* 5 untuk pilihan 'Pulang Besok'
* 3 untuk pilihan 'Pulang Lusa'
dll

### Kesimpulan

Menampilkan hasil perhitungan DSS dengan metoda Grid-Analisys



