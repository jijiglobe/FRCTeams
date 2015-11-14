import query

#Calculates a team's average score at event with code: <code> in <year>
def getAverageScore(team, year, code):
    matches = query.getAllMatches(year,code)
    teamkey = "frc"+str(team)
    ans = 0
    count  = 0
    for x in matches:
        for y in x["alliances"]["blue"]["teams"]:
            if y == teamkey:
                ans+= x["alliances"]["blue"]["score"]
                count+=1
        for y in x["alliances"]["red"]["teams"]:
            if y == teamkey:
                ans+= x["alliances"]["red"]["score"]
                count+=1
    return (0.0+ans)/(0.0+count)

#calculates a team's qualification score at an event
def getAverageQualScore(team, year, code):
    matches = query.getAllMatches(year,code)
    teamkey = "frc"+str(team)
    ans = 0
    count  = 0
    for x in matches:
        if x["comp_level"] == "qm" or x["comp_level"] == "ef":
            for y in x["alliances"]["blue"]["teams"]:
                if y == teamkey:
                    ans+= x["alliances"]["blue"]["score"]
                    count+=1
            for y in x["alliances"]["red"]["teams"]:
                if y == teamkey:
                    ans+= x["alliances"]["red"]["score"]
                    count+=1
    return (0.0+ans)/(0.0+count)

def getAverageQualScore(team, year):
    teamkey = "frc"+str(team)
    ans = 0
    count  = 0
    for event in query.getTeamEventList(team, year):
        matches = query.getAllMatches(year,event["event_code"])
        for x in matches:
            if x["comp_level"] == "qm" or x["comp_level"] == "ef":
                for y in x["alliances"]["blue"]["teams"]:
                    if y == teamkey:
                        ans+= x["alliances"]["blue"]["score"]
                        count+=1
                for y in x["alliances"]["red"]["teams"]:
                    if y == teamkey:
                        ans+= x["alliances"]["red"]["score"]
                        count+=1
    return (0.0+ans)/(0.0+count)

#calculates a team's average elimination score at an event        
def getAverageElimScore(team, year, code):
    matches = query.getAllMatches(year,code)
    teamkey = "frc"+str(team)
    ans = 0
    count  = 0
    for x in matches:
        if not( x["comp_level"] == "qm" or x["comp_level"] == "ef"):
            for y in x["alliances"]["blue"]["teams"]:
                if y == teamkey:
                    ans+= x["alliances"]["blue"]["score"]
                    count+=1
            for y in x["alliances"]["red"]["teams"]:
                if y == teamkey:
                    ans+= x["alliances"]["red"]["score"]
                    count+=1
    return (0.0+ans)/(0.0+count)

def getAverageElimScore(team, year):
    teamkey = "frc"+str(team)
    ans = 0
    count  = 0
    for event in query.getTeamEventList(team, year):
        matches = query.getAllMatches(year,event["event_code"])
        for x in matches:
            if not( x["comp_level"] == "qm" or x["comp_level"] == "ef"):
                for y in x["alliances"]["blue"]["teams"]:
                    if y == teamkey:
                        ans+= x["alliances"]["blue"]["score"]
                        count+=1
                for y in x["alliances"]["red"]["teams"]:
                    if y == teamkey:
                        ans+= x["alliances"]["red"]["score"]
                        count+=1
    return (0.0+ans)/(0.0+count)
    
print getAverageQualScore(694,2015)
