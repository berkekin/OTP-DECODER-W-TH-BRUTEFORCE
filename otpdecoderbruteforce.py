import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit
from PyQt6.QtCore import Qt

def decode(ciphertext, key):
    decrypted_text = ''
    for c, k in zip(ciphertext, key):
        decrypted_text += chr(((ord(c) - ord('A')) - (ord(k) - ord('A')) + 26) % 26 + ord('A'))
    return decrypted_text

class OTPDecoder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.ciphertext_input = QLineEdit()
        self.ciphertext_input.setPlaceholderText("Şifrelenmiş Metni Girin (Büyük Harflerle!) - Enter Encrypted Text (In Capital Letters!)")

        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Anahtar Metni Girin (Büyük Harflerle, Şifrelenmiş Metinle Aynı Uzunlukta) - Enter Key Text (In Capital Letters, Same Length as Encrypted Text) ")

        self.decode_button = QPushButton("Deşife Et - Decode")
        self.decode_button.clicked.connect(self.decode)

        self.brute_force_button = QPushButton(" Kaba kuvvet ile deşifre et - Decrypt With Brute Force")
        self.brute_force_button.clicked.connect(self.brute_force)

        self.decrypted_input = QTextEdit()
        self.decrypted_input.setPlaceholderText("Çözülmüş Metini Girin (Brute Force Sonuçlarında Bu Metin'e Ait Anahtar Aranır Girildiği Takdirde Anahtar Ve Ona Ait Çözülmüş Ve Şifreli Metin Gösterilir Boş Bırakılırsa Tüm Brute Force Sonuçları Yinede Kaydedilir. Opsiyonel.) - The key belonging to this text is searched in the Brute Force Results. If entered, the key and its decrypted and encrypted text are shown. If left blank, all Brute Force Results are still saved. Optional.)")

        self.result_label = QLabel()

        layout.addWidget(self.ciphertext_input)
        layout.addWidget(self.key_input)
        layout.addWidget(self.decode_button)
        layout.addWidget(self.brute_force_button)
        layout.addWidget(self.decrypted_input)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle("OTP Decoder With Brute Force ")
        self.showMaximized()
        self.show()

    def decode(self):
        ciphertext = self.ciphertext_input.text()
        key = self.key_input.text()
        decrypted_input = self.decrypted_input.toPlainText()

        if len(ciphertext) != len(key):
            self.result_label.setText("Hata: Şifrelenmiş metin ve anahtarın uzunluğu eşit olmalıdır. - Error: The length of the ciphertext and the key must be equal.")
            return

        plaintext = decode(ciphertext, key)
        if decrypted_input and plaintext != decrypted_input:
            self.result_label.setText("Hata: Girilen çözülmüş metin, şifreyi çözülen metinle eşleşmiyor. - Error: The entered decrypted text does not match the decrypted text.")
            return

        self.result_label.setText(f'Anahtar - Key: {key}, Şifreli Metin - Ciphertext: {ciphertext}, Çözülmüş Metin - Decoded Text: {plaintext}')

    def brute_force(self):
        ciphertext = self.ciphertext_input.text()
        possible_keys = 26 ** len(ciphertext)
        self.result_label.setText(f"Brute force işlemi başlıyor... Toplam {possible_keys} olası anahtar kombinasyonu deneniyor. - Brute force process begins... Total possible key combinations are tried.")

        found_keys = []
        with open("brute_force_results.txt", "w") as file:
            for i in range(possible_keys):
                key = num_to_base(i, 26).zfill(len(ciphertext))
                plaintext = decode(ciphertext, key)
                file.write(f"Anahtar: {key}, Metin: {plaintext}\n")
                if plaintext == self.decrypted_input.toPlainText():
                    found_keys.append((key, plaintext))
                percent_complete = (i + 1) / possible_keys * 100
                self.result_label.setText(f"Brute force işlemi devam ediyor... Tamamlanma Yüzdesi - Brute force operation continues... Percent Complete:: {percent_complete:.2f}%")
                QApplication.processEvents()  # Ekranı güncellemek için gereklidir

        if found_keys:
            self.result_label.setText("Bulunan Anahtarlar - Found Keys:")
            for key, plaintext in found_keys:
                self.result_label.setText(f'Anahtar - Key: {key}, Şifreli Metin - Ciphertext: {ciphertext}, Çözülmüş Metin - Decoded Text: {plaintext}')
        else:
            self.result_label.setText("Anahtar bulunamadı. - Key not found.")

def num_to_base(n, base):
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    while n:
        result = digits[n % base] + result
        n //= base
    return result or 'A'

def main():
    app = QApplication(sys.argv)
    window = OTPDecoder()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()