from celery import Celery

app = Celery('celery_calc', backend='redis://localhost:6379', broker='redis://localhost:6379')


@app.task
def suma(num1, num2):
    return num1 + num2


@app.task
def resta(num1, num2):
    return num1 - num2


@app.task
def mult(num1, num2):
    return num1 * num2


@app.task
def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    return "Invalid operation"


@app.task
def pot(num1, num2):
    return num1 ** num2
