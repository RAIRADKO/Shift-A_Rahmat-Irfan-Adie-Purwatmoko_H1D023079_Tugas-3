import datetime
import random

def main():
    tasks = []
    
    while True:
        print("\n=== Aplikasi Manajemen Tugas ===")
        print("1. Tambah Tugas Baru")
        print("2. Lihat Daftar Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1-4): ")
        
        # Struktur kontrol if-elif-else
        if pilihan == '1':
            # Generate ID acak menggunakan library random
            task_id = random.randint(1000, 9999)
            nama = input("Nama tugas: ")
            
            # Validasi tanggal menggunakan library datetime
            while True:
                try:
                    deadline = input("Deadline (YYYY-MM-DD): ")
                    deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Format tanggal salah! Gunakan format YYYY-MM-DD")
            
            # Struktur data dictionary untuk menyimpan informasi tugas
            tugas = {
                'id': task_id,
                'nama': nama,
                'deadline': deadline,
                'status': 'Belum Selesai'
            }
            tasks.append(tugas)
            print(f"Tugas berhasil ditambahkan dengan ID: {task_id}")
        
        elif pilihan == '2':
            # Struktur kontrol for loop
            print("\nDaftar Tugas:")
            for idx, tugas in enumerate(tasks, 1):
                print(f"{idx}. ID: {tugas['id']}")
                print(f"   Nama: {tugas['nama']}")
                print(f"   Deadline: {tugas['deadline']}")
                print(f"   Status: {tugas['status']}")
                print("-" * 30)
        
        elif pilihan == '3':
            task_id = int(input("Masukkan ID tugas yang selesai: "))
            # Struktur kontrol for loop dengan break
            for tugas in tasks:
                if tugas['id'] == task_id:
                    tugas['status'] = 'Selesai'
                    print(f"Tugas ID {task_id} ditandai selesai!")
                    break
            else:
                print("ID tugas tidak ditemukan!")
        
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-4")

if __name__ == "__main__":
    main()
