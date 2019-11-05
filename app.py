from random import randrange

from flask import Flask, render_template

from data_access.pg_data_access import PgDataAccess, PgDbParams
app = Flask(__name__)
PG = {

    "PG_HOST": "localhost",
    "PG_USER": "postgres",
    "PG_PORT": 5432,
    "PG_PASS": "postgres",
    "PG_DB_NAME": "IG_TEST"

}
db_params = PgDbParams(PG)
db_access = PgDataAccess(db_params)

def get_img():
    query="""SELECT media_url FROM ig_instagram_posts  where media_url != '' order by id desc limit 100"""
    return db_access.execute_query_with_return(query)[randrange(100)][0]
@app.route('/')
def hello_world():
    return render_template("index.html", img=get_img())


if __name__ == '__main__':
    app.run()
