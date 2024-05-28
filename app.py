from flask import Flask, jsonify, request

app = Flask(__name__)

# Livros
books = [{
    'id': 1,
    'title': 'Duna : Livro 1',
    'author': 'Frank Herbert'
},
    {'id': 2,
     'title': 'O Festim dos Corvos',
     'author': "George R. R. Martin"
     },
    {'id': 3,
     'title': 'O Guia do Mochileiro das Galáxias',
     'author': "Douglas Adams"
     }
]

# Consultar livros


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

 # Consultar por id


@app.route('/books/<int:id>', methods=['GET'])
def get_book_id(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Livro não encontrado"}), 404

 # Editar


@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    book_edit = request.get_json()
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book.update(book_edit)
        return jsonify({"message": "Livro alterado com sucesso"}), 200
    return jsonify({"error": "Livro não encotrado"}), 404

# Criar livro


@app.route('/books', methods=['POST'])
def create_new_book():
    new_book = request.get_json()
    if 'id' not in new_book or 'title' not in new_book or 'author' not in new_book:
        return jsonify({"Error": "Dados incompletos"}), 400
    books.append(new_book)
    return jsonify({"message": f"{new_book['title']} foi adicionado com sucesso!"}), 201

# Excluir


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = next((book for book in book if book['id'] == id), None)
    if book:
        books.remove(book)
        return jsonify({"message": "Livro deletado com sucessso"}), 200

    return jsonify({"error": "Livro não encontrado"}), 404


app.run(port=5000, host='localhost', debug=True)
