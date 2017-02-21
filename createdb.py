from pony.orm import *
from pony.orm.serialization import to_json
from flask_cors import CORS, cross_origin



db = Database()


class Team_1(db.Entity):
    id = PrimaryKey(int, auto=True)
    teamid = Required(unicode)
    Name = Required(unicode)
    country = Required(unicode)
   




db.bind("sqlite", "database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)	

@db_session
def llenandobase():
    Team_1(teamid = u"1",Name = u"Barcelona",country =u"Spain")
    Team_1(teamid = u"2",Name = u"Real Madrid",country =u"Spain")
    Team_1(teamid = u"3",Name = u"Sevilla",country = u"Spain")
    Team_1(teamid = u"4",Name = u"Atletico Madrid",country =u"Spain")
    Team_1(teamid = u"5",Name = u"Real Sociedad",country = u"Spain")
    Team_1(teamid = u"6",Name = u"Eibar",country = u"Spain")
    Team_1(teamid = u"7",Name = u"Celta de Vigo",country = u"Spain")
    Team_1(teamid = u"8", Name = u"Athletic Club",country = u"Spain")
    Team_1(teamid = u"9", Name = u"Valencia",country = u"Spain")
    Team_1(teamid = u"10", Name = u"Villareal",country = u"Spain")
    Team_1(teamid = u"11", Name= u"Malaga", country = u"Spain")
    Team_1(teamid = u"12", Name = u"Alaves", country = u"Spain")
    Team_1(teamid = u"13", Name = u"Sporting", country = u"Spain")
    Team_1(teamid = u"14",Name = u"Leganes", country = u"Spain")
    Team_1(teamid = u"15",Name = u"Granada", country = u"Spain")
    Team_1(teamid = u"16",Name = u"Las Palmas",country = u"Spain")
    Team_1(teamid = u"17",Name = u"Osasuna",country = u"Spain")
    Team_1(teamid = u"18",Name = u"Espanyol",country = u"Spain")
    Team_1(teamid = u"19",Name = u"Real Betis",country = u"Spain")
    Team_1(teamid = u"20",Name = u"Deportivo",country = u"Spain")



if __name__ == '__main__':
	llenandobase()
	




