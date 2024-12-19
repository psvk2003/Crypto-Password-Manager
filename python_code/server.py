from flask import Flask, render_template, request, jsonify
from Crypto.Protocol.KDF import PBKDF2
from sha256 import generate_hash
from aes import encrypt, decrypt
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

SECRET_KEY = b'SECRET_KEY'

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            domain VARCHAR(255) PRIMARY KEY,
            ciphertext TEXT,
            hashed_master_password TEXT
        )
    ''')

def save_data_to_db(cursor, conn, encrypted_data):
    for domain, item in encrypted_data.items():
        cursor.execute('''
            INSERT INTO passwords (domain, ciphertext, hashed_master_password)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE ciphertext = VALUES(ciphertext), hashed_master_password = VALUES(hashed_master_password)
        ''', (domain, item['ciphertext'], item['hashed_master_password']))
    conn.commit()

def load_data_from_db(cursor):
    cursor.execute('SELECT * FROM passwords')
    data = {row[0]: {'ciphertext': row[1], 'hashed_master_password': row[2]} for row in cursor.fetchall()}
    return data

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Mohit@6669',
            database='pm_ap'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store_password', methods=['POST'])
def store_password():
    data = request.get_json()

    # Validate that required fields are present
    if not all(key in data for key in ('domain', 'password', 'masterPassword')):
        return jsonify({'error': 'Missing required fields'})

    # Validate that fields are not empty
    if any(data[key] == '' for key in ('domain', 'password', 'masterPassword')):
        return jsonify({'error': 'Fields cannot be empty'})

    domain = data['domain']
    password = data['password']
    master_password = data['masterPassword']

    # Hash the master password before storing it
    hashed_master_password = generate_hash(master_password.encode()).hex()

    key = PBKDF2(hashed_master_password.encode(), SECRET_KEY, dkLen=32, count=1000000)

    ciphertext = encrypt(key, password)

    conn = connect_to_mysql()
    if conn:
        cursor = conn.cursor()
        create_table(cursor)

        encrypted_data = load_data_from_db(cursor)
        encrypted_data[domain] = {
            'ciphertext': ciphertext.hex(),
            'hashed_master_password': hashed_master_password,
        }

        save_data_to_db(cursor, conn, encrypted_data)

        cursor.close()
        conn.close()

        return jsonify({'message': 'Password stored successfully'})

    return jsonify({'error': 'Failed to connect to MySQL database'})

@app.route('/retrieve_password', methods=['POST'])
def retrieve_password():
    data = request.get_json()

    # Validate that required fields are present
    if not all(key in data for key in ('domain', 'masterPassword')):
        return jsonify({'error': 'Missing required fields'})

    # Validate that fields are not empty
    if any(data[key] == '' for key in ('domain', 'masterPassword')):
        return jsonify({'error': 'Fields cannot be empty'})

    domain = data['domain']
    master_password = data['masterPassword']

    conn = connect_to_mysql()
    if conn:
        cursor = conn.cursor()
        encrypted_data = load_data_from_db(cursor)

        try:
            encrypted_item = encrypted_data[domain]
        except KeyError:
            return jsonify({'error': 'Domain not found'})

        ciphertext = bytes.fromhex(encrypted_item['ciphertext'])
        hashed_master_password = encrypted_item['hashed_master_password']

        # Check if the provided master password is correct
        if generate_hash(master_password.encode()).hex() != hashed_master_password:
            return jsonify({'error': 'Incorrect master password'})

        # Use the hashed master password for key derivation
        key = PBKDF2(hashed_master_password.encode(), SECRET_KEY, dkLen=32, count=1000000)

        try:
            plaintext = decrypt(key, ciphertext)
            plaintext_str = plaintext.decode('utf-8')
        except Exception as e:
            return jsonify({'error': str(e)})

        cursor.close()
        conn.close()

        return jsonify({'password': plaintext_str})

    return jsonify({'error': 'Failed to connect to MySQL database'})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    cert = 'C:\\Users\\hp\\Desktop\\sem5\\cryptography\\A_6_end\\python_code\\cert.pem'
    key = 'C:\\Users\\hp\\Desktop\\sem5\\cryptography\\A_6_end\\python_code\\key.pem'
    app.run(host='0.0.0.0', port=5000, debug=True,ssl_context = (cert,key))
