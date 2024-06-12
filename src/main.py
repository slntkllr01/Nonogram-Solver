from inputParser import *
from bfSolver import *
from btSolver import *
import time

def main():
    print("\n--- NANOGRAM SOLVER ---\n")
    
    while True:
        file = str(input("Masukkan nama file untuk di-solve ! (type 'E' for exit) "))

        if file == 'E' or file == 'e':
            print("\nTerima kasih telah menggunakan program ini! See Ya! \n")
            break
        
        n, row_hints, col_hints = inputParser("test/" + file)
        
        if n is None:
            print("\nSilakan input ulang nama file yang sesuai!\n")
        else:
            print("\n[1] Brute Force")
            print("[2] Runut-Balik (Backtracking)\n")
            while True:
                algo = int(input("Masukkan jenis algoritma yang ingin digunakan ! [1 / 2] "))
                if (algo == 1):
                    start_time = time.perf_counter()
                    bruteforceSolver(row_hints, col_hints, n)
                    end_time = time.perf_counter()
                    duration = (end_time - start_time) * 1000
                    print("\nDurasi: {:.3f} ms".format(duration))
                    break
                elif (algo == 2):
                    start_time = time.perf_counter()
                    backtrackingSolverMain(row_hints, col_hints)
                    end_time = time.perf_counter()
                    duration = (end_time - start_time) * 1000
                    print("\nDurasi: {:.3f} ms".format(duration))
                    break       
                else:
                    print("Masukkan angka yang valid!")
                    continue
            
        

# Panggil fungsi utama
if __name__ == "__main__":
    main()
