from flask import Flask, jsonify,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/employee'
db=SQLAlchemy(app)


class Employee(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    Designation=db.Column(db.String(100),nullable=False)


    def __repr__(self):
        return f"<Employee(id={self.id}, name={self.name}, age={self.age}, gender={self.gender}, Designation={self.Designation})>"
    








@app.route("/",methods=['GET','POST'])
def home():

    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        gender=request.form.get("gender")
        des=request.form.get("designation")

        
        details=Employee(name=name,age=age,gender=gender,Designation=des)

        try:
            db.session.add(details)
            db.session.commit()
            redirect("")
        except:
            return "Error"
        print(name,age,gender,des)
        redirect("/")

    details=Employee.query.all()
    print(details)
    return render_template("index.html",details=details)

@app.route("/delete/<int:id>")
def delete(id):
    emp=Employee.query.get_or_404(id)
    try:
        db.session.delete(emp)
        db.session.commit()
        return redirect("/")
    except:
        return "error"


    
    

@app.route("/update/<int:id>",methods=['POST','GET'])
def update(id):
    emp=Employee.query.get_or_404(id)

    emp_data = {
        'id': emp.id,
        'name': emp.name,
        'age': emp.age,
        'des': emp.Designation,
        'gender': emp.gender,
       
    }
    if request.method=='POST':
        print("emp",emp)
        emp.name=request.form["name"]
        emp.age=request.form["age"]
        emp.gender=request.form["gender"]
        emp.Designation=request.form["designation"]

        try:
            db.session.commit()
            return redirect("/")
        except:
            return "update Failed"
        

    return jsonify({'message': 'Employee updated successfully','emp':emp_data})

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
