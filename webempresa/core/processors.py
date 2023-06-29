from datetime import datetime

def year_now(request):
    dateNow = datetime.now()
    yearNow = datetime.strftime(dateNow, '%Y')

    ctx = {'yearNow': int(yearNow)}

    return ctx
