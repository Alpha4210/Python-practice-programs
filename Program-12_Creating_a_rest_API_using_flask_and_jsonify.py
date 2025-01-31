from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/armstrong/<int:num>")
def armstrong(num):
    #Check if a number is an armstrong number - the numner is equal to the sum of the digits of the number raised to the power of the number of digits of the number.
    x = 0 #Saves the number calculated for checking with the given number
    
    # Calculating the number
    
    for i in str(num):
        x = int(i)**3+x
           
    # Checking if its armstrong number
    if x==int(num):
        print(f"{num} is an armstrong number")
        return jsonify(armstrong = True,
                       number = num,
                       )
    else:
        print("It is not a armstrong number")
        return jsonify(armstrong = False,
                       number = num,
                        )
                
if __name__=="__main__":
    app.run(debug=True)