import json, urllib2, httplib
domain = "www.thebluealliance.com"
api = "/api/v2/%s"
hdr = {"X-TBA-App-Id": "frc694:testing-app:v01"}

#Gets teamNumber's team information formatted as follows:
#    {"website": Team's official website URL,
#    "name": longform name of team",
#    "nickname": Teams nickname or functional name,
#    "locality": Team's city,
#    "region": Team's state or region,
#    "team_number": Team's number,
#    "location": Longform locality address,
#    "country_name": Name of team's country,
#    "rookie_year": Team's rookie year"}

def getTeamData(teamNumber):
    conn = httplib.HTTPConnection(domain)
    path = "team/frc"+str(teamNumber)
    conn.request("GET",api % path ,headers = hdr)
    r = conn.getresponse()
    answer = r.read().decode('utf-8')
    return json.loads(answer)

#helper function to take an  array of matches (as retrieved in getAllMatches()) and converts to URL strings
def getVideoList(array):
    ans = []
    for x in array:
        if x["type"] == "youtube":
            ans += "www.youtube.com/watch?v="+x["key"]
    return ans

#Returns the requested event data from the requested year as follows:
#    {"name": name of event,
#    "short_name": short name of event,
#    "event_type-string": string defining event type,
#    "event_district-string": string defining disctrict of event,
#    "location": Longform address of city,
#    "venue_address": Longform address of the venue,
#    "website": event website string,
#    "teams": dictionary of teams at event(formatted as above in getTeamData),
#    "matches": dictionary of match data(formatted as below in getMatchData),
#    "alliances": Json array of alliances:
#                 "picks": [captain,team2,team3]
#                 "declines": [team1,team2, team3]
def getEventData(year, code):
    conn = httplib.HTTPConnection(domain)
    path = "event/"+str(year)+code
    conn.request("GET",api % path ,headers = hdr)
    r = conn.getresponse()
    answer = r.read().decode('utf-8')
    final = json.loads(answer)
    return final
    
#returns list of matches formatted as:
#    {"key": match key,
#    "comp_level": level of competition ie qm,em,qf,sf,f,
#    "alliances": {
#        "blue": {
#            "score": match score
#            "teams": list of team keys ie [frc1, frc694, frc9999]
#        }
#        "red": {
#            "score": match score
#            "teams": list of team keys ie [frc1, frc694, frc9999]
#        }
#    "videos" JSON array of available match videos
#    "time_string": string of time scheduled for match,
#    "time": Unix time scheduled for match}
def getAllMatches(year, code):
    conn = httplib.HTTPConnection(domain)
    path = "event/"+str(year)+code+"/matches"
    conn.request("GET",api % path ,headers = hdr)
    r = conn.getresponse()
    answer = r.read().decode('utf-8')
    final = json.loads(answer)
    for x in final:
        x["videos"] = getVideoList(x["videos"])
    return final

#takes an element of getAllMatches List and returns the match scores as follows:
#    {"blue": score for blue,
#    "red: score for red}
def getMatchScore(match):
    return {"blue": match["score_breakdown"]["blue"]["total_points"],
            "red": match["score_breakdown"]["red"]["total_points"]
    }
    
print getEventData(2015,"nyny")
