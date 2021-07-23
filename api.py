from app.utils.settings import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from app.routes.studentRoutes import *
from app.routes.teacherRoute import *
if __name__ == "__main__":
    app.run(port=3000, debug=True)