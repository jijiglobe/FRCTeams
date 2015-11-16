from flask import Flask, render_template, request, redirect, url_for

import data
import query

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/@<teamNum>", methods=["GET", "POST"])
@app.route("/@<teamNum>/", methods=["GET", "POST"])
def main(teamNum=-1):
    """
    This is the main method for the web app. If the teamNum variable is not set,
    or is not a valid team number, the web app will render a different page.
    Otherwise, it will render the page, providing a dictionary with basic team
    info and a dictionary of score results.
    """
    if request.method == "POST":
        return redirect("/@%s" % (str(request.form["team"])))
    if teamNum == -1:
        return render_template("start_page.html")
    if not teamNum.isdigit():
        return render_template("invalid_team.html", TEAM=teamNum)
    team = int(teamNum)
    if not query.isExistingTeam(team):
        return render_template("inexistent_team.html", TEAM=teamNum)
    if query.isInactiveTeam(team):
        return render_template("inactive_team.html", TEAM=teamNum)
    teamBasicData = query.getTeamData(team)
    return render_template("team.html", BASIC=teamBasicData)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
