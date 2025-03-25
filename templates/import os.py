import os

def kirim_file(file_path, alasan):
    try:
        # Cek apakah file ada di lokasi yang ditentukan
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File tidak ditemukan: {file_path}")

        # Logika untuk mengirim file dan alasan masuk divisi
        # Misalnya, mengirim file melalui email atau menyimpannya ke server
        print(f"Mengirim file: {file_path}")
        print(f"Alasan masuk divisi: {alasan}")

        # Contoh pengiriman file (sesuaikan dengan kebutuhan Anda)
        # send_file_via_email(file_path, alasan)

    except FileNotFoundError as e:
        print(e)
        # Tindakan yang diambil jika file tidak ditemukan
        # Misalnya, meminta pengguna untuk mengunggah ulang file
        print("Silakan unggah ulang file yang benar.")

# Contoh penggunaan fungsi
file_path = "path/to/your/file.txt"
alasan = "Saya ingin bergabung dengan divisi ini karena..."
kirim_file(file_path, alasan)