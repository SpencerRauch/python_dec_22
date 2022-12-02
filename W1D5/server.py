from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "No secrets on github"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/form') #DISPLAY ROUTE
def display_form():
    return render_template("form.html")

@app.route('/process', methods=['POST']) #ACTION ROUTE
def process():
    # if request.method == 'POST':
    #     pass
    print("Now charging you a bunch of money")
    print(request.form)
    session['name'] = request.form['name']
    session['cuisine'] = request.form['cuisine']
    #NEVER RENDER A TEMPLATE ON AN ACTION ROUTE
    return redirect('/display')
    # return render_template("display.html", name=request.form['name'], cuisine=request.form['cuisine']) #DO NOT DO THIS

@app.route('/display')
def display_results():
    if 'name' in session:
        name = session['name']
    else:
        name = "Not provided"
    if not 'cuisine' in session:
        session['cuisine'] = "Not provided"
    return render_template("display.html", name=name)

@app.route('/reset') #ACTION
def reset():
    # del session['name']
    session.clear()
    return redirect('/form')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  



"""
so the name you set for the input is the key in the immutable multi dictionary the form generates

YES

"""