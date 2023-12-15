import json

class LaporanKeuangan:
    @staticmethod
    def simpan_laporan(pencatat, nama_file):
        laporan = {
            "saldo": pencatat.saldo,
            "riwayat_transaksi": pencatat.riwayat_transaksi
        }

        with open(nama_file, 'w') as file:
            json.dump(laporan, file)

        print("Laporan transaksi berhasil disimpan.")

    @staticmethod
    def baca_laporan(nama_file):
        try:
            with open(nama_file, 'r') as file:
                laporan = json.load(file)
                saldo = laporan.get("saldo", 0)
                riwayat_transaksi = laporan.get("riwayat_transaksi", [])

                print("Laporan transaksi berhasil dibaca.")
                return saldo, riwayat_transaksi
        except FileNotFoundError:
            print("File laporan tidak ditemukan.")
            return None, None
        except json.JSONDecodeError:
            print("Format file laporan tidak valid.")
            return None, None
