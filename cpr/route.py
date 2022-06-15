import json
from msilib import type_short
from cpr.getSkills import getSkillsF
from cpr.getUsers import getUsers
from cpr.processPrecentage import processPer
from flask import flash, redirect, render_template, url_for, request, jsonify
from flask import session
from cpr import app, db, bcrypt, processSkills
from cpr.form import RegistrationFrom, LoginFrom, RecruterLoginFrom, RecruterRegistrationFrom
from cpr.models import User, Ruser, Tech
from flask_login import login_user, current_user, logout_user

global user


@app.route("/")
def hero():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):

            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', form=form)


@app.route('/about-us')
def aboutUs():
    return render_template('aboutUs.html')


@app.route('/get-started', methods=['POST', 'GET'])
def getStarted():
    if(request.method == 'POST'):
        allSkills = json.loads(request.data)
        email = allSkills['user']
        tech = allSkills['itechno']
        allSkills1 = allSkills['tskills']
        dictTech = processSkills.processSkillsFunct(allSkills1)
        dictPer = processPer(allSkills1, dictTech, tech)
        session["dictTech"] = dictTech
        session["dictPer"] = dictPer
        l = list(dictTech.keys())
        user_id = User.query.filter_by(email=allSkills['user']).first()
        if len(l) == 1:
            if Tech.query.filter_by(user_id=user_id.id).first() == None:
                t1 = Tech(tech1=l[0], user_id=user_id.id)
                db.session.add(t1)
                db.session.commit()
            else:
                t1 = Tech.query.filter_by(user_id=user_id.id).first()
                t1.tech1 = l[0]
                db.session.commit()

        elif len(l) == 2:
            if Tech.query.filter_by(user_id=user_id.id).first() == None:
                t2 = Tech(tech1=l[0], tech2=l[1], user_id=user_id.id)
                db.session.add(t2)
                db.session.commit()
            else:
                t2 = Tech.query.filter_by(user_id=user_id.id).first()
                t2.tech1 = l[0]
                t2.tech2 = l[1]
                db.session.commit()

        elif len(l) == 3:
            if Tech.query.filter_by(user_id=user_id.id).first() == None:
                t3 = Tech(tech1=l[0], tech2=l[1],
                          tech3=l[2], user_id=user_id.id)
                db.session.add(t3)
                db.session.commit()
            else:
                t3 = Tech.query.filter_by(user_id=user_id.id).first()
                t3.tech1 = l[0]
                t3.tech2 = l[1]
                t3.tech3 = l[2]
                db.session.commit()

        elif len(l) == 4:
            if Tech.query.filter_by(user_id=user_id.id).first() == None:
                t4 = Tech(tech1=l[0], tech2=l[1], tech3=l[2],
                          tech4=l[3], user_id=user_id.id)
                db.session.add(t4)
                db.session.commit()
            else:
                t4 = Tech.query.filter_by(user_id=user_id.id).first()
                t4.tech1 = l[0]
                t4.tech2 = l[1]
                t4.tech3 = l[2]
                t4.tech4 = l[3]

        elif len(l) == 5:
            if Tech.query.filter_by(user_id=user_id.id).first() == None:
                t5 = Tech(tech1=l[0], tech2=l[1],
                          tech3=l[2], tech4=l[3], tech5=l[4], user_id=user_id.id)
                db.session.add(t5)
                db.session.commit()
            else:
                t5 = Tech.query.filter_by(user_id=user_id.id).first()
                t5.tech1 = l[0]
                t5.tech2 = l[1]
                t5.tech3 = l[2]
                t5.tech4 = l[3]
                t5.tech5 = l[4]
                db.session.commit()

        elif len(l) == 6:
            if Tech.query.filter_by(user_id=user_id.id).first() == None:
                t6 = Tech(tech1=l[0], tech2=l[1], tech3=l[2],
                          tech4=l[3], tech5=l[4], tech6=l[5], user_id=user_id.id)
                db.session.add(t6)
                db.session.commit()
            else:
                t6 = Tech.query.filter_by(user_id=user_id.id).first()
                t6.tech1 = l[0]
                t6.tech2 = l[1]
                t6.tech3 = l[2]
                t6.tech4 = l[3]
                t6.tech5 = l[4]
                t6.tech6 = l[5]
                db.session.commit()

        elif len(l) == 7:
            if Tech.query.filter_by(user_id=user_id.id).first() == None:
                t7 = Tech(tech1=l[0], tech2=l[1], tech3=l[2],
                          tech4=l[3], tech5=l[4], tech6=l[5], tech7=l[6], user_id=user_id.id)
                db.session.add(t7)
                db.session.commit()
            else:
                t7 = Tech.query.filter_by(user_id=user_id.id).first()
                t7.tech1 = l[0]
                t7.tech2 = l[1]
                t7.tech3 = l[2]
                t7.tech4 = l[3]
                t7.tech5 = l[4]
                t7.tech6 = l[5]
                t7.tech7 = l[6]
                db.session.commit()
        elif len(l) == 8:
            if Tech.query.filter_by(user_id=user_id.id).first() == None:
                t8 = Tech(tech1=l[0], tech2=l[1], tech3=l[2], tech4=l[3],
                          tech5=l[4], tech6=l[5], tech7=l[6], tech8=l[7], user_id=user_id.id)
                db.session.add(t8)
                db.session.commit()
            else:
                t8 = Tech.query.filter_by(user_id=user_id.id).first()
                t8.tech1 = l[0]
                t8.tech2 = l[1]
                t8.tech3 = l[2]
                t8.tech4 = l[3]
                t8.tech5 = l[4]
                t8.tech6 = l[5]
                t8.tech7 = l[6]
                t8.tech8 = l[7]
                db.session.commit()
        elif len(l) == 9:
            if Tech.query.filter_by(user_id=user_id.id).first() == None:
                t9 = Tech(tech1=l[0], tech2=l[1], tech3=l[2], tech4=l[3],
                          tech5=l[4], tech6=l[5], tech7=l[6], tech8=l[7], tech9=l[8], user_id=user_id.id)
                db.session.add(t9)
                db.session.commit()
            else:
                t9 = Tech.query.filter_by(user_id=user_id.id).first()
                t9.tech1 = l[0]
                t9.tech2 = l[1]
                t9.tech3 = l[2]
                t9.tech4 = l[3]
                t9.tech5 = l[4]
                t9.tech6 = l[5]
                t9.tech7 = l[6]
                t9.tech8 = l[7]
                t9.tech9 = l[8]
                db.session.commit()

        elif len(l) >= 10:
            if Tech.query.filter_by(user_id=user_id.id) == None:
                t10 = Tech(tech1=l[0], tech2=l[1], tech3=l[2], tech4=l[3], tech5=l[4],
                           tech6=l[5], tech7=l[6], tech8=l[7], tech9=l[8], tech10=l[9], user_id=user_id.id)
                db.session.add(t10)
                db.session.commit()
            else:
                t10 = Tech.query.filter_by(user_id=user_id.id).first()
                t10.tech1 = l[0]
                t10.tech2 = l[1]
                t10.tech3 = l[2]
                t10.tech4 = l[3]
                t10.tech5 = l[4]
                t10.tech6 = l[5]
                t10.tech7 = l[6]
                t10.tech8 = l[7]
                t10.tech9 = l[8]
                t10.tech10 = l[9]
                db.session.commit()
        dictionaries = {"dictT": dictTech, "dictP": dictPer}
        return jsonify(dictionaries)

    return render_template('getStarted.html')


@app.route("/loading-page")
def loadingPage():
    return render_template('loadingPage.html')


@app.route('/output', methods=['GET', 'POST'])
def outputF():
    if request.method == 'GET':
        return render_template("output.html")


@app.route('/get-to-know', methods=['GET', 'POST'])
def getToKnow():
    if request.method == 'POST':
        jobole = json.loads(request.data)
        skills = getSkillsF(jobole)
        return jsonify({"skills": skills})
    return render_template('getToKnow.html')


@app.route('/Logout')
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for("hero"))
    logout_user()
    return redirect(url_for('hero'))


@app.route('/rregister', methods=['GET', 'POST'])
def rregister():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RecruterRegistrationFrom()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = Ruser(companyname=form.companyname.data, username=form.username.data,
                     email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('rlogin'))
    return render_template('rregister.html', form=form)


@app.route('/rlogin', methods=["GET", "POST"])
def rlogin():
    if current_user.is_authenticated:
        return redirect(url_for("rhome"))
    form = RecruterLoginFrom()
    if form.validate_on_submit():
        user = Ruser.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('rhome'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('rlogin.html', form=form)


@app.route('/recruiter-home', methods=["GET", "POST"])
def rhome():
    if request.method == 'POST':
        tech = json.loads(request.data)
        print(tech)
        user = getUsers(tech)
        return jsonify(user)

    return render_template('rhome.html')
