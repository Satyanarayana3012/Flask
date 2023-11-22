import sqlite3
import sqlalchemy
from flask import Flask, request, jsonify
import database
import exception

app = Flask(__name__)

@app.route("/bank/account/", methods=["POST"])

def create_account():
    data = request.json
    try:
        name= data["name"]
        balance= data["balance"]
        aadhaar= data["aadhaar"]
    except KeyError as e:
        err = exception.InvalidData()
        return err.message, err.status
    try:
        database.save_account(name,balance,aadhaar)
    except sqlalchemy.exc.IntegrityError as e:
        return "Name already exists", 400
    acc_no = database.get_accno(name)
    return str({
        "accno":acc_no
    }), 200

@app.route("/bank/account/<int:accno>", methods=["PUT"])
def update_account(accno):
    data = request.json
    name = data.get("name", None)
    aadhaar = data.get("aadhaar",None)

    try:
        account = database.Update_account(accno,name,aadhaar)
    except sqlalchemy.exc.IntegrityError as e:
        return str({"status": 500,
                    "message": "internal database error"}), 500
    return str(account), 200
@app.route("/bank/account/balance/<int:accno>",methods = ["PUT"])
def debit(accno):
    data = request.json
    operation = data.get("operation", "credit")

    return str(database.Update_balance(accno, True if operation == 'debit'  else False if operation == 'credit' else str('error'),data.get('amount', 0))), 200

@app.route("/bank/account/<int:accno>", methods=["GET"])
def get_account(accno):
    account = database.get_Account(accno)
    if account:
        return str(account), 200
    else:
        return str({"status":404,
                    "message":"Account not found"
                    })
@app.route("/bank/account/<int:accno>",methods=["DELETE"])
def delete_account(accno):
    try:
        result = database.delete(accno)
    except sqlalchemy.exc.IntegrityError as e:
        return str({"status": 500,
                    "message": "internal database error"}), 500
    if result:
        return str({
            "status":200,
            "message":"Deleted"
        }), 200
    else:
        return str({
            "status":404,
            "message":"Account not found"
        }),404
@app.route("/bank/fetchall", methods=["GET"])
def fetch_all():
    accounts = database.get_all()
    response = {}
    for account in accounts:
        response[account.accno] = [account.name,account.balance,account.aadhaar]
        return str(response), 200
app.run(debug=True)