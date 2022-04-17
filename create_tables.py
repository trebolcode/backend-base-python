from config.database import Base, engine
from app.models.items import Item


def main():
    print("Creating database...")

    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
