import query

def getAverageScore(team, year, code):
    """
    Calculates a team's average score at event with code: <code> in <year>
    """
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

def getAverageQualScore(team, year, code):
    """
    Calculates a team's qualification score at an event
    """
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
        for match in matches:
            if match["comp_level"] == "qm" or match["comp_level"] == "ef":
                for mteam in match["alliances"]["blue"]["teams"]:
                    if mteam == teamkey:
                        ans += match["alliances"]["blue"]["score"]
                        count += 1
                for mteam in match["alliances"]["red"]["teams"]:
                    if mteam == teamkey:
                        ans +=  match["alliances"]["red"]["score"]
                        count += 1
    return (float(ans))/(float(count))

def getAverageElimScore(team, year, code):
    """
    Calculates a team's average elimination score at an event
    """
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
