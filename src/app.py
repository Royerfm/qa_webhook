from flask import Flask, request, jsonify
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

print(f"SECRET_TOKEN cargado: {app.config['SECRET_TOKEN']}")


@app.route('/webhook', methods=['POST'])
def webhook():
    # Verificar el token secreto en el encabezado
    secret_token = request.headers.get('Authorization')
    if secret_token != f"Bearer {app.config['SECRET_TOKEN']}":
        return jsonify({"error": "Unauthorized"}), 401

    # Procesar los datos del evento
    event_data = request.get_json()
    if not event_data:
        return jsonify({"error": "Invalid payload"}), 400

    # Log de los datos recibidos
    print("Evento recibido:", event_data)

    # Responder al WebHook
    return jsonify({"message": "Evento recibido correctamente"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
