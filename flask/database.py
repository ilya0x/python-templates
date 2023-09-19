from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text

# * Create your database engine:
# * If using mysql:
# * create_engine("mysql+pymysql://user:pass@localhost/dbname?charset=utf8mb4", echo=True, future=True)

engine = create_engine(
    "mysql+pymysql:///db/name.db",
    connect_args={
        "ssl": {
            "ca": "/home/gord/client-ssl/ca.pem",
            "cert": "/home/gord/client-ssl/client-cert.pem",
            "key": "/home/gord/client-ssl/client-key.pem"
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("select * form Enrollment2020"))
    print(result.all())
