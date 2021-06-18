from flask import Flask, render_template, request

app = Flask(__name__)


# This is an example of the api routes. Can add methods to do CRUD (Create, Read, Update, Delete)
@app.route('/', methods=['GET', 'POST'])
def hello():
    page = 1
    hello_text = 'Hello Dan!'

    if request.method == 'POST':
        print('post')

    # this is how you pass the info to HTML. You pass in the html page with data.
    return render_template(
        'hello_dan.html',
        hello_text=hello_text,
        page=page
    )


@app.route('/another-page')
def hello_other():
    page = 2
    hello_text = 'Hello Other Page!'
    return render_template(
        'hello_dan.html',
        hello_text=hello_text,
        page=page
    )


if __name__ == '__main__':
    app.run()
