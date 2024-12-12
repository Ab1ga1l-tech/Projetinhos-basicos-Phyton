from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para armazenar as tarefas
lista = [
    {
        'tarefa': 'andar'
    }
]

# Função para adicionar uma tarefa
@app.route('/tarefa', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.json.get("tarefa")
    if nova_tarefa:
        lista.append(nova_tarefa)
        return jsonify({"message": f"Tarefa '{nova_tarefa}' adicionada com sucesso!"}), 201
    else:
        return jsonify({"error": "Nenhuma tarefa fornecida."}), 400

# Função para ver as tarefas
@app.route('/tarefas', methods=['GET'])
def ver_tarefas():
    if lista:
        return jsonify({"tarefas": lista}), 200
    else:
        return jsonify({"message": "Nenhuma tarefa pendente."}), 200

# Função para excluir uma tarefa
@app.route('/tarefa/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    if 0 <= id < len(lista):
        excluída = lista.pop(id)
        return jsonify({"message": f"Tarefa '{excluída}' excluída."}), 200
    else:
        return jsonify({"error": "Tarefa não encontrada."}), 404

# Função para marcar tarefa como concluída
@app.route('/tarefa/<int:id>/concluir', methods=['PUT'])
def concluir_tarefa(id):
    if 0 <= id < len(lista):
        lista[id] = lista[id] + " (concluída)"
        return jsonify({"message": f"Tarefa '{lista[id]}' marcada como concluída."}), 200
    else:
        return jsonify({"error": "Tarefa não encontrada."}), 404

# Rota principal para verificar se a API está funcionando
@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo à To-Do List API!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
