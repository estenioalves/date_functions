from datetime import datetime


def today():
    today = datetime.now()
    return today


def verify_date(date):
    try:
        date_format = datetime.strptime(date, "%d/%m/%Y")
        return date_format
    except:
        raise Exception("Formato de data errado. Insere DIA-MES-ANO")


def verify_due(date_ref):
    due_date = verify_date(date=date_ref)
    if today() > due_date:
        return "Data expirou"
    else:
        return "Data não expirou"
