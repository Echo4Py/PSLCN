from flask import Flask, render_template
from jinja2 import Template
import time
from filecmp import cmp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('namelist')

@app.route('/list')
def fn():
    import os
    fl = os.listdir(r'FILESYSTEM')
    with open(r'templates/namelist', 'w+') as f:
        for i in fl:
            f.write(i+'<br />')
    f.close()

@app.route('/filesystem')
def fs():
    return render_template('filesystem')
    
def monitor_size():
    from filecmp import cmp
    #import commands
    result1 = cmp('FILESYSTEM/filesystem', 'templates/filesystem')
    if result1 == bool(0):
        app.run()
        #commands.getoutput('python main.py runserver')

def dur(op=None, clock=[time.time()]):
    if op != None:
        duration = time.time() - clock[0]
        print ('%s Finished. Duration %.2f Seconds.') % op, duration
        #print('{0} Finished. Duration {1:.2f} Seconds.'.format(op,duration))
    clock[0] = time.time()
    return dur
        
if __name__ == ('__main__'):
    dur()
    fn()
    monitor_size()
    app.run()
    dur('restart    :')
    #app.run(debug=True)
