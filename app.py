from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)




# MySQL yapılandırması
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'amazon-test'

mysql = MySQL(app)

@app.route('/add-product', methods=['POST'])
def add_product():
    data = request.json
    name = data['name']
    description = data['description']
    price = data['price']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO products(name, description, price) VALUES (%s, %s, %s)", (name, description, price))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Ürün başarıyla eklendi'}), 201

if __name__ == '__main__':
    app.run(debug=True)
