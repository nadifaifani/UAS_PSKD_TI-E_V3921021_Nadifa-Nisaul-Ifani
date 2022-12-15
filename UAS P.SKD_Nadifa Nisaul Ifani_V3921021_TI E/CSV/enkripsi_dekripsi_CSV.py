# import modul
from cryptography.fernet import Fernet


# key generation
key = Fernet.generate_key()
 
# read string kunci
with open('CSV/filekunci.key', 'wb') as filekey:
   filekey.write(key)


# pakai kunci
fernet = Fernet(key)
 
# buka file csv
with open('D:/KULIAH/SEMESTER 3/PRAKTIK SISTEM KEAMANAN DATA/UAS/CSV/file_csv.csv', 'rb') as file:
    original = file.read()
     
# enkripsi csv
encrypted = fernet.encrypt(original)
 
# simpan file enkripsi
with open('D:/KULIAH/SEMESTER 3/PRAKTIK SISTEM KEAMANAN DATA/UAS/CSV/hasil/enkrip.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


#DEKRIPSI
    
# pakai kunci yang tadi
fernet = Fernet(key)

# buka file hasil enkrpisi
with open('D:/KULIAH/SEMESTER 3/PRAKTIK SISTEM KEAMANAN DATA/UAS/CSV/hasil/enkrip.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# langsung di dekripsi 
decrypted = fernet.decrypt(encrypted)

# cek hasil dekripsi cocok apa tidak ??
with open('D:/KULIAH/SEMESTER 3/PRAKTIK SISTEM KEAMANAN DATA/UAS/CSV/hasil/deskrip.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
