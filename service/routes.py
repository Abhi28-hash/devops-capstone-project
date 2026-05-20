from flask import Flask, jsonify, request
from service.models import Account

app = Flask(__name__)


@app.route("/accounts", methods=["POST"])
def create_account():
    data = request.get_json()

    account = Account(
        name=data["name"],
        email=data["email"]
    )

    account.create()

    return jsonify({
        "id": account.id,
        "name": account.name,
        "email": account.email
    }), 201


@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):

    account = Account.find(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    return jsonify({
        "id": account.id,
        "name": account.name,
        "email": account.email
    }), 200


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):

    account = Account.find(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json()

    account.name = data["name"]
    account.email = data["email"]

    account.update()

    return jsonify({
        "id": account.id,
        "name": account.name,
        "email": account.email
    }), 200


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):

    account = Account.find(account_id)

    if not account:
        return jsonify({"error": "Account not found"}), 404

    account.delete()

    return "", 204


@app.route("/accounts", methods=["GET"])
def list_accounts():

    accounts = Account.list_all()

    results = []

    for account in accounts:
        results.append({
            "id": account.id,
            "name": account.name,
            "email": account.email
        })

    return jsonify(results), 200


if __name__ == "__main__":
    app.run(debug=True)