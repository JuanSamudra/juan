import tkinter as tk
from tkinter import messagebox

def simpan_data():
    nim = entry_nim.get()
    nama = entry_nama.get()
    prodi = entry_prodi.get()
    semester = entry_semester.get()
    ipk1 = entry_ipk1.get()
    ipk2 = entry_ipk2.get()

    if not (nim and nama and prodi and semester and ipk1 and ipk2):
        messagebox.showwarning("Peringatan", "Semua data harus diisi!")
        return

    try:
        ipk1 = float(ipk1)
        ipk2 = float(ipk2)
    except ValueError:
        messagebox.showerror("Error", "IPK harus berupa angka!")
        return

    # Simpan data (misalnya, ke file atau database)
    messagebox.showinfo("Informasi", f"Data berhasil disimpan:\nNIM: {nim}\nNama: {nama}\nProdi: {prodi}\nSemester: {semester}\nIPK Semester 1: {ipk1}\nIPK Semester 2: {ipk2}")

# Membuat jendela utama
root = tk.Tk()
root.title("Data Mahasiswa")

# Label dan Entry untuk setiap data
label_nim = tk.Label(root, text="NIM")
label_nim.grid(row=0, column=0, padx=10, pady=5)
entry_nim = tk.Entry(root)
entry_nim.grid(row=0, column=1, padx=10, pady=5)

label_nama = tk.Label(root, text="Nama")
label_nama.grid(row=1, column=0, padx=10, pady=5)
entry_nama = tk.Entry(root)
entry_nama.grid(row=1, column=1, padx=10, pady=5)

label_prodi = tk.Label(root, text="Prodi")
label_prodi.grid(row=2, column=0, padx=10, pady=5)
entry_prodi = tk.Entry(root)
entry_prodi.grid(row=2, column=1, padx=10, pady=5)

label_semester = tk.Label(root, text="Semester")
label_semester.grid(row=3, column=0, padx=10, pady=5)
entry_semester = tk.Entry(root)
entry_semester.grid(row=3, column=1, padx=10, pady=5)

label_ipk1 = tk.Label(root, text="IPK Semester 1")
label_ipk1.grid(row=4, column=0, padx=10, pady=5)
entry_ipk1 = tk.Entry(root)
entry_ipk1.grid(row=4, column=1, padx=10, pady=5)

label_ipk2 = tk.Label(root, text="IPK Semester 2")
label_ipk2.grid(row=5, column=0, padx=10, pady=5)
entry_ipk2 = tk.Entry(root)
entry_ipk2.grid(row=5, column=1, padx=10, pady=5)

# Tombol Simpan
btn_simpan = tk.Button(root, text="SIMPAN", command=simpan_data)
btn_simpan.grid(row=6, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()