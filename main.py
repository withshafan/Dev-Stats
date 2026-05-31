from flask import Flask, render_template, request
from app.api import get_user, get_repos
from db_core import init_db, save_user, save_repos, get_saved_users
from app.calc import calc_language_stats, calc_engagement, prepare_repo_data

# flask app banayein
app = Flask(__name__, template_folder="app/templates")

# main web page ka route
@app.route("/", methods=["GET", "POST"])
def home():
    # variables initialize karein
    usr = None
    rep = []       # <--- YAHAN YE NAYI LINE ADD KAREIN
    st_stars = 0
    st_forks = 0
    l_stat = {}
    err = None

    # agar web form submit kiya gaya hai
    if request.method == "POST":
        # form se username nikalein
        u_name = request.form.get("username")
        usr = get_user(u_name)

        if usr:
            # github se repos mangwayein
            rep = get_repos(u_name)

            # db mein data save karein
            u_id = save_user(usr["login"], usr["followers"])
            r_dat = prepare_repo_data(u_id, rep)
            save_repos(u_id, r_dat)

            # stats calculate karein
            st_stars, st_forks = calc_engagement(rep)
            l_stat = calc_language_stats(rep)
        else:
            # agar user na mile
            err = "GitHub user nahi mila. Spelling check karein."

    # db se purane saved users nikalein
    s_usr = get_saved_users()

    # html page ko data bhejein
    return render_template(
        "dashboard.html", 
        user=usr, 
        stars=st_stars, 
        forks=st_forks, 
        langs=l_stat, 
        saved=s_usr, 
        error=err,
        repos=rep # ye line add karein
    )

if __name__ == "__main__":
    # app start hone se pehle db setup karein
    init_db()
    
    # server ko start karein
    app.run(debug=True)