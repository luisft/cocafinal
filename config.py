import web

db_host = 'uoa25ublaow4obx5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'd6oajj4x7mo9pqzi'
db_user = 'o3okz8niv9nfmpmd'
db_pw = 'pt367kcevj2ljpa1'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )