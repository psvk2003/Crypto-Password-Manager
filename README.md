# Crypto-Password-Manager
A secure password management system built with Flask, SHA-256 hashing, PBKDF2 key derivation, and AES encryption for robust data protection.

## Introduction
Crypto Password-Manager is a secure and user-friendly application designed to manage passwords efficiently. Built using Flask, it employs advanced cryptographic techniques like SHA-256 hashing, PBKDF2 key derivation, and AES encryption to ensure data security. 

The system allows users to securely store and retrieve passwords through a simple web interface. It prioritizes data confidentiality by storing only hashed master passwords and encrypted data. This project is a robust solution for modern password management challenges.

Through meticulous implementation of the Advanced Encryption Standard (AES) and a custom SHA-256 hashing algorithm, we establish a formidable defense against unauthorized access and potential data breaches.

## Proposed Methodology
<h3>Web Framework Selection</h3>:
Flask, a lightweight and extensible web framework, is chosen for its simplicity and flexibility in handling HTTP requests. It facilitates the creation of web applications with minimal boilerplate code.
Password Security Measures:
The master password is hashed using the SHA-256 algorithm, a widely accepted and secure hashing function. Hashing provides a one-way transformation, enhancing the security of stored passwords.

<h3>Key Derivation with PBKDF2</h3>:
The PBKDF2 key derivation function is applied to the hashed master password for generating an encryption key. This process introduces computational complexity, making it resistant to brute-force attacks and enhancing key security.

<h3>AES Encryption</h3>:
The Advanced Encryption Standard (AES) is employed for encrypting passwords. AES is a symmetric encryption algorithm widely recognized for its security and efficiency.

<h3>Secure Password Storage</h3>:
Encrypted passwords are securely stored, and only the hashed master password is stored for verification purposes. This adds an additional layer of security, as even if the stored data is compromised, it would be challenging to retrieve the original master password.

<h3>Web API Endpoints for Operations</h3>:
The application exposes two main endpoints - one for storing passwords securely and another for retrieving passwords. These endpoints follow best practices for handling JSON data and provide a simple yet effective interface for password management.

<h3>Error Handling and User Feedback</h3>:
The code includes error handling mechanisms to provide meaningful feedback to users, ensuring a smooth an user-friendly experience. This is essential for effective communication in case of incorrect inputs or potential issues.

## AES Encryption:
The flowchart shows the steps involved in encrypting a block of data (plaintext) using the AES algorithm. The first step is to add the plaintext to the initial key (K0). This is followed by nine rounds of transformations.

![image](https://github.com/user-attachments/assets/c0741ea4-afb6-4e9b-90a4-4381eddb05dd)

### SHA 256
![image](https://github.com/user-attachments/assets/71db8404-b89b-44c5-bca1-86616719cac3)

### Implementation
![image](https://github.com/user-attachments/assets/5ce45ced-20a9-4645-9860-6ec1ec73895d)

### Website
![image](https://github.com/user-attachments/assets/0f7e9930-42cf-4ff5-81f5-41105dbcd0c4)
![image](https://github.com/user-attachments/assets/48505a13-a3e1-4fc6-91b4-293b175a5b78)
![image](https://github.com/user-attachments/assets/4a81aa48-73c1-4f46-b29f-373a0c9c97e2)

## Future Work
In advancing this password management system, several key areas warrant exploration. First, the integration of biometric authentication can enhance user convenience and security. Additionally, the implementation of a robust intrusion detection system and anomaly detection algorithms will fortify the application against evolving cyber threats. Enhancing scalability through cloud-based storage solutions and exploring blockchain for decentralized security measures are avenues for consideration. To improve user experience, incorporating a comprehensive password strength evaluation mechanism and refining the user interface for mobile responsiveness will be beneficial. Lastly, continuous security audits and adherence to emerging cryptographic standards will ensure the system remains resilient in the face of emerging threats, contributing to a sustainable and secure password management solution.







