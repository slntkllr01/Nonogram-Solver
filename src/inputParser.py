def inputParser(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            
            # Validasi jumlah baris
            if len(lines) < 2:
                print("File tidak valid: Jumlah baris tidak mencukupi.")
                return None, None, None
            
            # membaca kolom dan baris (ukuran grid)
            try:
                n = int(lines[0])
            except ValueError:
                print("File tidak valid: Baris pertama harus berisi 1 angka jumlah ukuran grid!")
                return None, None, None

            # Validasi ukuran grid
            if n <= 0:
                print("File tidak valid: Ukuran grid harus lebih besar dari nol.")
                return None, None, None

            # Validasi jumlah total baris dalam file
            if len(lines) < (2 * n + 3):
                print("File tidak valid: Jumlah baris tidak mencukupi untuk memuat semua hints.")
                return None, None, None

            # membaca row hints
            row_hints = []
            for i in range(2, n + 2):
                try:
                    row_hints.append(list(map(int, lines[i].strip().split())))
                except ValueError:
                    print(f"File tidak valid: Row hints pada baris {i+1} tidak valid.")
                    return None, None, None

            # membaca col hints
            col_hints = []
            for i in range(n + 3, 2 * n + 3):
                try:
                    col_hints.append(list(map(int, lines[i].strip().split())))
                except ValueError:
                    print(f"File tidak valid: Col hints pada baris {i+1} tidak valid.")
                    return None, None, None

            # Validasi konten hints
            for hints in row_hints + col_hints:
                for num in hints:
                    if num < 0:
                        print("File tidak valid: Petunjuk harus berupa angka positif.")
                        return None, None, None

            return n, row_hints, col_hints

    except FileNotFoundError:
        print(f"\nFile '{path}' tidak ditemukan.")
        return None, None, None