from create import Account,Session

def get_accno(name):
    accno = Session.query(Account.accno).filter_by(name=name).one_or_none()
    return accno[0]
def get_all():
    accounts = Session.query(Account)
    return accounts
def save_account(name,balance,aadhar):
    account = Account(name=name, balance=balance, aadhaar=aadhar)
    Session.add(account)
    Session.commit()
def Update_account(name,aadhaar):
    account = Session.query(Account).filter_by(name=name).one_or_none()
    account.name = name
    account.aadhaar = aadhaar
    Session.commit()

def Update_balance(accno,debit,amount):
    account = Session.query(Account).filter_by(accno=accno).one_or_none()
    if debit == 'error':
        return str({'status': 400,
                    'message': 'Invalid debit'})
    if(debit):
            account.balance -= amount
    else:
        account.balance += amount
    Session.commit()
    return account
def get_Account(accno):
    account = Session.query(Account).filter_by(accno=accno).one_or_none()
    return account
def delete(accno):
    account = Session.query(Account).filter_by(accno=accno).one_or_none()
    if account:
        Session.delete(account)
        Session.commit()
        return "Success"
    else:
        return "No such account found!"