# from typing import List
#
# from sqlalchemy import delete
# from sqlalchemy.orm import Session
# from ..schemas.product_schema import ProductCreate, ProductDTO
# from ..models.product_model import Product
#
#
# def create_product(db: Session, product: ProductCreate) -> Product:
#     db_product = Product(
#         name=product.name,
#         price=product.price,
#         availability=product.availability,
#         details=product.details,
#     )
#     db.add(db_product)
#     db.commit()
#
#     return db_product
#
#
# def get_all_products(db: Session) -> List[ProductDTO]:
#     products = db.query(Product).all()
#     return products
#
#
# def get_product_by_id(db: Session, product_id: int) -> Product:
#     query = db.query(Product).filter(Product.id == product_id).first()
#     return query
#
#
# def delete_user(db: Session, product_id: int) -> None:
#     query = (
#         delete(Product)
#         .where(Product.id == product_id)
#         .execution_options(synchronize_session="fetch")
#     )
#     db.execute(query)
#     db.commit()
