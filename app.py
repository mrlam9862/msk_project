from flask import Flask

#--- __name__ 
app = Flask(__name__)
# bulid Flask wen page format
@app.route("/")

# from requests import PandaRequest

def index():
    # print("Hello Word")
    # return
    return('re Hello Word')
    
app.run()