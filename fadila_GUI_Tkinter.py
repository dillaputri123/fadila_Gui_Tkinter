import tkinter as tk
from tkinter import messagebox

def submit_data():
    nim = entry_23100706.get()
    nama = entry_fadila_putri.get()
    prodi = entry_teknik_informatika.get()
    semester = entry_3.get()
    ipk_semester1 = entry_80_semester1.get()
    ipk_semester2 = entry_86_semester2.get()

    # Menampilkan data yang diinputkan
    messagebox.showinfo("Data yang Dimasukkan", 
                        f"NIM: {NIM_23100706}\nNama: {NAMA_FADILA_PUTRI}\nProdi: {PRODI_TEKNIK_INFORMATIKA}\nSemester: {semester3}\nIPK Semester 1: {ipk80_semester1}\nIPK Semester 2: {ipk86_semester2}")

# Membuat jendela utama
root = tk.Tk()
root.title("FORM DATA MAHASISWA")

# Membuat label dan entry untuk NIM
label_nim = tk.Label(root, text="NIM 23100706:")
label_nim.grid(row=0, column=0, padx=10, pady=10)
entry_nim = tk.Entry(root)
entry_nim.grid(row=0, column=1, padx=10, pady=10)

# Membuat label dan entry untuk Nama
label_nama = tk.Label(root, text="NAMA FADILA PUTRI:")
label_nama.grid(row=1, column=0, padx=10, pady=10)
entry_nama = tk.Entry(root)
entry_nama.grid(row=1, column=1, padx=10, pady=10)

# Membuat label dan entry untuk Prodi
label_prodi = tk.Label(root, text="PRODI TEKNIK INFORMATIKA:")
label_prodi.grid(row=2, column=0, padx=10, pady=10)
entry_prodi = tk.Entry(root)
entry_prodi.grid(row=2, column=1, padx=10, pady=10)

# Membuat label dan entry untuk Semester
label_semester = tk.Label(root, text="SEMESTER 3:")
label_semester.grid(row=3, column=0, padx=10, pady=10)
entry_semester = tk.Entry(root)
entry_semester.grid(row=3, column=1, padx=10, pady=10)

# Membuat label dan entry untuk IPK Semester 1
label_ipk_semester1 = tk.Label(root, text="IPK Semester 1 80:")
label_ipk_semester1.grid(row=4, column=0, padx=10, pady=10)
entry_ipk_semester1 = tk.Entry(root)
entry_ipk_semester1.grid(row=4, column=1, padx=10, pady=10)

# Membuat label dan entry untuk IPK Semester 2
label_ipk_semester2 = tk.Label(root, text="IPK Semester 2 86:")
label_ipk_semester2.grid(row=5, column=0, padx=10, pady=10)
entry_ipk_semester2 = tk.Entry(root)
entry_ipk_semester2.grid(row=5, column=1, padx=10, pady=10)

# Membuat tombol untuk submit data
button_submit = tk.Button(root, text="SIMPAN", command=submit_data)
button_submit.grid(row=6, columnspan=2, pady=20)

# Menjalankan aplikasi
root.mainloop()