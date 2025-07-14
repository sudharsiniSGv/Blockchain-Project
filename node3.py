
from flask import Flask, jsonify, request, render_template, redirect
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

# Node ID
node_address = 'Node3'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mine_block')
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender='System', receiver=node_address, amount=1)
    block = blockchain.create_block(proof, previous_hash)
    blockchain.replace_chain()
    return redirect('/')

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    sender = request.form['sender']
    receiver = request.form['receiver']
    amount = int(request.form['amount'])
    blockchain.add_transaction(sender, receiver, amount)
    return redirect('/')

@app.route('/replace_chain')
def replace_chain():
    blockchain.replace_chain()
    return redirect('/')

@app.route('/get_chain')
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    # Auto-connect peers on start
    blockchain.add_node('http://127.0.0.1:5001')
    blockchain.add_node('http://127.0.0.1:5002')
    blockchain.add_node('http://127.0.0.1:5004')
    app.run(host='0.0.0.0', port=5003)
