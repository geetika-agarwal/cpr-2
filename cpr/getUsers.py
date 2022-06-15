from cpr.models import Tech,User

def getUsers(tech):
    
    l=[]
    d={}
    if(Tech.query.filter(Tech.tech1 == tech).all() != None):
        for i in Tech.query.filter(Tech.tech1 == tech).all():
            l.append(User.query.filter_by(id=i.user_id).first())
    if(Tech.query.filter(Tech.tech2 == tech).all() != None):
        for i in Tech.query.filter(Tech.tech2 == tech).all():
            l.append(User.query.filter_by(id=i.user_id).first())
    if(Tech.query.filter(Tech.tech3 == tech).all() != None):
        for i in Tech.query.filter(Tech.tech3 == tech).all():
            l.append(User.query.filter_by(id=i.user_id).first())
    if(Tech.query.filter(Tech.tech4 == tech).all() != None):
        for i in Tech.query.filter(Tech.tech4 == tech).all():
            l.append(User.query.filter_by(id=i.user_id).first())
    if(Tech.query.filter(Tech.tech5 == tech).all() != None):
        for i in Tech.query.filter(Tech.tech5 == tech).all():
            l.append(User.query.filter_by(id=i.user_id).first())
    if(Tech.query.filter(Tech.tech6 == tech).all() != None):
        for i in Tech.query.filter(Tech.tech6 == tech).all():
            l.append(User.query.filter_by(id=i.user_id).first())
    if(Tech.query.filter(Tech.tech7 == tech).all() != None):
        for i in Tech.query.filter(Tech.tech7 == tech).all():
            l.append(User.query.filter_by(id=i.user_id).first())
    if(Tech.query.filter(Tech.tech8 == tech).all() != None):
        for i in Tech.query.filter(Tech.tech8 == tech).all():
            l.append(User.query.filter_by(id=i.user_id).first())
    if (Tech.query.filter(Tech.tech9 == tech).all() != None):
        for i in Tech.query.filter(Tech.tech9 == tech).all():
            l.append(User.query.filter_by(id=i.user_id).first())
    if (Tech.query.filter(Tech.tech10 == tech).all() != None):
        for i in Tech.query.filter(Tech.tech10 == tech).all():
            l.append(User.query.filter_by(id=i.user_id).first())
    if l==[]:
        return []
    else :
        for i in l:
             d[i.email] = i.username


    return d  

