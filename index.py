#from flask import Flask
from flask import Flask, redirect, url_for, request
 
# https://www.wintellect.com/containerize-python-app-5-minutes/

app = Flask(__name__)

@app.route('/success/<name>') 
def success(name): 
   return 'welcome %s' % name 
  
@app.route('/login',methods = ['POST', 'GET']) 
# Sample request --> http:localhost:5000/login?nm=surajit
def login(): 
   if request.method == 'POST': 
      user = request.form['nm']
      
      # Final redirecting to '@app.route('/success/<name>')'
      print("+++++++++++ Under POST call, redirecting to /success/", user)
      return redirect(url_for('success',name = user)) 
   else: 
      user = request.args.get('nm')
      print("+++++++++++++++ Under GET call, final redirecting to /success/", user)
      
      # Final redirecting to '@app.route('/success/<name>')'
      return redirect(url_for('success',name = user)) 
  
if __name__ == '__main__': 
   app.run(host="0.0.0.0", port=int("5000"), debug=True) 