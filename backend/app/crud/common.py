from sqlalchemy.orm import Session


def list_all(db: Session, model):
    return db.query(model).all()


def get_one(db: Session, model, item_id: str):
    return db.query(model).filter(model.id == item_id).first()


def create_one(db: Session, model, payload):
    item = model(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_one(db: Session, item, payload):
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item


def delete_one(db: Session, item):
    db.delete(item)
    db.commit()
    return item
