from modules.SQLAlchemy import sql_alchemy
from states import states_runner

sql_alchemy.init_setup()
states_runner.run()
