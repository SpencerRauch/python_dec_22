from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")  # Return the string 'Hello World!' as a response

@app.route('/new_route')
def new_route():
    return "Hey look a different route"

@app.route('/hello/<name>')
def hi_name(name):
    return f"Hello, {name}"

@app.route('/hello/<name_param>/<int:times>')
def hi_name_times(name_param, times):
    # return f"<p>Hello, {name} \n <p>" * times
    return render_template("hi_name.html", name=name_param, times=times, color="peachpuff")

@app.route('/list')
def list():

    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    return render_template("list.html", list=student_info)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,port=5001,host="0.0.0.0")    # Run the app in debug mode.