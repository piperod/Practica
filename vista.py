from pony.orm import *
from pony.orm.serialization import to_json



db = Database()


class Team_1(db.Entity):
    id = PrimaryKey(int, auto=True)
    teamid = Required(unicode)
    Name = Required(unicode)
    country = Required(unicode)
    ps = Set('Players_1')


class Players_1(db.Entity):
    id = PrimaryKey(int, auto=True)
    Name = Required(unicode)
    teamid = Required(unicode)
    team_1 = Required(Team_1)


db.bind("sqlite", "database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)	





from flask import Flask, jsonify
app = Flask(__name__)



@app.route('/table',methods = ['POST','GET'])
@db_session 
def index():

    list = Team_1.select()
    
    return to_json(list)
@db_session
def llenandobase():
	Team_1(teamid = u"1",Name = u"Fc Barcelona",country = u"Spain" )
	Team_1(teamid = u"2",Name = u"Real Madrid",country = u"Spain" )
	Team_1(teamid = u"3",Name = u"Manchester City",country = u"England" )
	Team_1(teamid = u"4",Name = u"Chelsea FC",country = u"England" )
	Players_1(Name =u"Leo Messi",teamid = u"1")
	Players_1(Name =u"Cristiano Ronaldo",teamid = u"2")

if __name__ == '__main__':
	llenandobase()
	app.run(debug = True)




