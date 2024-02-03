# OTP-DECODER-W-TH-BRUTEFORCE

USE FOR EDUCATİONAL PURPOSES ONLY! - SADECE EĞİTİM AMAÇLI KULLANINIZ!


EN: This code is a PyQt6 application with a user interface that serves as an OTP (One-Time Pad) Decoder. OTP is a cipher method that encrypts the text using a completely random key and relies on each key being used only once, hence it's also known as a "single-use cipher block".

This application provides the following main features to the user:

Encryption and Decryption: The user can encrypt or decrypt the text by entering the encrypted text and the key. Encryption and decryption operations are performed by clicking the "Decode" button.

Decryption with Brute Force: If the user does not enter the encrypted text or the key, they can decrypt the text using brute force method. Clicking the "Decrypt With Brute Force" button initiates the brute force process. This process tries all possible key combinations.

Detailed Feedback: During the brute force process, detailed feedback such as completion percentage is provided to the user. This gives the user an idea of how long the process will take and tracks progress during the process.

Verification of Decrypted Text: The user can verify the accuracy of the brute force process by entering the decrypted text during the brute force process. If the entered decrypted text matches a decrypted text found during the brute force process, the corresponding key and decrypted text are displayed to the user.

Brute Force Results: All keys and decrypted texts found during the brute force process are saved to a file named "brute_force_results.txt". This maintains a record of the results for the user to review or analyze later.

This application provides a user-friendly interface and simple functionality to serve as an easily understandable learning tool about OTP encryption.




 



TR: Bu kod, PyQt6 kütüphanesi kullanılarak oluşturulmuş bir arayüze sahip bir OTP (One-Time Pad) Decoder uygulamasıdır. OTP, güvenli ve tamamen rastgele bir anahtar kullanılarak metni şifreleyen ve her anahtarın sadece bir kez kullanılmasına dayanan bir şifreleme yöntemidir. Bu nedenle "tek kullanımlık şerit bloğu" olarak da bilinir.

Bu uygulama, kullanıcıya aşağıdaki ana özellikleri sunar:

Şifreleme ve Çözme: Kullanıcı, şifrelenmiş metni ve anahtarı girerek metni şifreleyebilir veya çözebilir. Şifreleme ve çözme işlemleri "Decode" düğmesine tıklanarak gerçekleştirilir.

Brute Force ile Çözme: Kullanıcı, şifrelenmiş metni girmezse veya anahtar belirtmezse, brute force yöntemini kullanarak metni çözebilir. "Kaba kuvvet ile deşifre et" düğmesine tıklanarak brute force işlemi başlatılır. Bu işlem, tüm olası anahtar kombinasyonlarını deneyerek gerçekleştirilir.

Detaylı Geri Bildirim: Brute force işlemi sırasında, kullanıcıya tamamlanma yüzdesi gibi detaylı geri bildirimler sağlanır. Bu, işlemin ne kadar süreceği konusunda kullanıcıya fikir verir ve işlem sırasında bir ilerleme izlenir.

Çözülen Metnin Kontrolü: Kullanıcı, brute force işlemi sırasında çözülen metni girerek, brute force işleminin doğruluğunu kontrol edebilir. Eğer girilen çözülen metin, brute force işlemi sonucunda bulunan bir anahtarla eşleşiyorsa, bu anahtar ve çözülmüş metin kullanıcıya gösterilir.

Brute Force Sonuçları: Brute force işlemi sonucunda bulunan tüm anahtarlar ve çözülmüş metinler, "brute_force_results.txt" adlı bir dosyaya kaydedilir. Bu, kullanıcının daha sonra gözden geçirmesi veya analiz etmesi için kayıtlı sonuçların bir kaydını tutar.

Bu uygulama, kullanıcı dostu bir arayüz ve basit bir işlevsellik ile OTP şifrelemesi hakkında anlaşılması kolay bir öğrenme aracı sağlar.


