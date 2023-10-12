def vigenere_encrypt(plain_text, key):
  encrypted_text = []
  key_length = len(key)
  for i in range(len(plain_text)):
    char = plain_text[i]
    key_char = key[i % key_length]
    char_code = ord(char)
    key_code = ord(key_char)
    encrypted_code = (char_code + key_code) % 26 + ord('A')
    encrypted_text.append(chr(encrypted_code))
  return ''.join(encrypted_text)


def vigenere_decrypt(encrypted_text, key):
  decrypted_text = []
  key_length = len(key)
  for i in range(len(encrypted_text)):
    char = encrypted_text[i]
    key_char = key[i % key_length]
    char_code = ord(char)
    key_code = ord(key_char)
    decrypted_code = (char_code - key_code) % 26 + ord('A')
    decrypted_text.append(chr(decrypted_code))
  return ''.join(decrypted_text)


def register_user(users, username, password, key):
  if username not in users:
    encrypted_password = vigenere_encrypt(password, key)
    users[username] = encrypted_password
    print("Pengguna {} telah terdaftar.".format(username))
  else:
    print("Pengguna dengan nama {} sudah ada.".format(username))


def login(users, username, password, key):
  if username in users:
    encrypted_password = vigenere_encrypt(password, key)
    if users[username] == encrypted_password:
      print("Login berhasil!")
    else:
      print("Kata sandi salah.")
  else:
    print("Nama pengguna tidak ditemukan.")


def main():
  users = {}  # Dictionary untuk menyimpan pengguna dan kata sandi terenkripsi
  key = "SECRET"  # Kunci Vigenère

  while True:
    print("simulasi login sederhana dengan enkripsi Vigenère Cipher by:  ")
    print("             Nama  : Ignasius Silaban")
    print("             Kelas : TI.21.C.5")

    print("Menu:")
    print("1. Daftar")
    print("2. Login")
    print("3. Keluar")
    choice = input("Pilih : ")

    if choice == "1":
      username = input("Masukkan nama pengguna: ")
      password = input("Masukkan kata sandi: ")
      register_user(users, username, password, key)

    elif choice == "2":
      username = input("Masukkan nama pengguna: ")
      password = input("Masukkan kata sandi: ")
      login(users, username, password, key)

    elif choice == "3":
      print("Keluar.")
      break
    else:
      print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
  main()
