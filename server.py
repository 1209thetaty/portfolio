from flask import Flask, render_template,request,url_for,redirect
import csv
app = Flask(__name__)
print(__name__)

#C:\Users\WarangkanaYoomieng\Documents\LOG-ISSUE-REPORT\PYTHON\WEB_DEV\server>venv\Scripts\activate
#set FLASK_APP=server
#set FLASK_ENV=development
#flask run

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/<username>/<int:post_id>')
def test_param(username=None,post_id=None):
    return render_template('index2.html',name=username,post_id=post_id)

@app.route('/blog')
def hello_world_test():
    return 'Boring blog!'

@app.route('/blog/2020/dogs')
def blog_test():
    return 'Wowwww 2020 DOGS!!'

@app.route('/<string:page_name>')
def html_page(page_name):
    name=f'{page_name}.html'
    return render_template(name)

def write_to_db_txt(data):
    with open('./venv/db.txt',mode='a') as db_file: # write in binary 
        email = data['email']
        subject = data['subject']
        message=data['message']
        print(f'Email : {email}  Subject : {subject}  Message : {message}')
        txt =f'{email}|{subject}|{message}\n'
        file= db_file.write(str(txt))
def write_to_db_csv(data):
    with open('db.csv',mode='a', newline='') as db_file: # write in binary 
        email = data['email']
        subject = data['subject']
        message=data['message']
        csv_writer = csv.writer(db_file,delimiter=',' ,quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:            
            data = request.form.to_dict()
            #write_to_db_txt(data)
            write_to_db_csv(data)
            message='Thank you for contacting me <3 '
        except:
            message = 'Something went wrong, I will check :('
        return render_template('/thank_you.html',message=message)
    else:
        return 'Theres something wrong'



