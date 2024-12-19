% Example AES Encryption and Decryption

% Encryption Key (128-bit key in hexadecimal)
encryptionKey = '2b7e151628aed2a6abf7158809cf4f3c';

% Input Message (128-bit plaintext in hexadecimal)
plaintext = '3243f6a8885a308d313198a2e0370734';
disp("Original Message")
disp(plaintext);
disp(" ")

% Encryption
ciphertext = Cipher(encryptionKey, plaintext);
disp('Ciphertext:');
disp(ciphertext);
disp(" ")

% Decryption
decryptedText = InvCipher(encryptionKey, ciphertext);
disp('Decrypted Text:');
disp(decryptedText);
