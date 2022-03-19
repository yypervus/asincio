import sqlalchemy

metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(f'sqlite:///asincbd.db')
connection = engine.connect()

stat_character = sqlalchemy.Table('stat_character', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column('birth_year', sqlalchemy.String(100)),
    sqlalchemy.Column('eye_color', sqlalchemy.String(100)),
    sqlalchemy.Column('films', sqlalchemy.Text()),
    sqlalchemy.Column('gender', sqlalchemy.String(100)),
    sqlalchemy.Column('hair_color', sqlalchemy.String(100)),
    sqlalchemy.Column('height', sqlalchemy.String(100)),
    sqlalchemy.Column('homeworld', sqlalchemy.Text()),
    sqlalchemy.Column('mass', sqlalchemy.String(100)),
    sqlalchemy.Column('name', sqlalchemy.String(100)),
    sqlalchemy.Column('skin_color', sqlalchemy.String(100)),
    sqlalchemy.Column('species', sqlalchemy.Text()),
    sqlalchemy.Column('starships', sqlalchemy.Text()),
    sqlalchemy.Column('vehicles', sqlalchemy.Text())
)

metadata.create_all(engine)