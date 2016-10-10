#References: 
#https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822

from flask import Flask, render_template
import datetime

 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')
 
if __name__ == '__main__':
  app.run(debug=True)



epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


print unix_time_millis(unix_time)