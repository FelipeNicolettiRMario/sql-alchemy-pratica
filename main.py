import sqlalchemy
from sqlalchemy.orm import Session
from entities.Author import Author

def main():
    engine = sqlalchemy.create_engine("mysql+mysqldb://root:1234@localhost:3306/library", echo=True)

    session = Session(engine)

    new_author = Author(name="Julio Verne",bio="French author",country="France")
    session.add(new_author)

    our_user = session.query(Author).filter_by(name='Julio Verne').first()

    if our_user == new_author:
        session.commit()

if __name__ == '__main__':
    main()