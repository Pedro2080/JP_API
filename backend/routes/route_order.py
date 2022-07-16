from fastapi import FastAPI

from typing import List, Optional


from fastapi import Depends, HTTPException
from fastapi import Response, APIRouter, status
from sqlalchemy.orm import Session

from ..crud import order_crud
from ..database.config import get_db
from ..schemas.order_schema import OrderCreate, OrderDTO


router = APIRouter()
feature_flag = "ORDER_ROUTE"


@router.post("/orders", response_model=OrderDTO)
async def create_order(
    response: Response, order: OrderCreate, db: Session = Depends(get_db)
):
    return order_crud.create_order(db=db, order=order)


@router.get("/orders", response_model=List[OrderDTO])
async def get_orders(db: Session = Depends(get_db)):

    return order_crud.get_all_orders(db=db)


@router.get("/orders/{order_id}", response_model=OrderDTO)
async def get_order_by_id(response: Response, order_id: int, db: Session = Depends(get_db)):
    order = order_crud.get_order_by_id(db=db, order_id=order_id)

    if not order:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:

        return order


@router.delete("/order/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: int, db: Session = Depends(get_db)):
    order_crud.delete_order(db=db, order_id=order_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
