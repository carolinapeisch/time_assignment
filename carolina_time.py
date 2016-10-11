#References: 
#https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822

from flask import Flask
import time
import sys
 
app = Flask(__name__)      
 
@app.route('/')
def get_time():
  return str(int(time.time()*1000))
 
if __name__ == '__main__':
  app.run(host="0.0.0.0", port=sys.argv[1])

