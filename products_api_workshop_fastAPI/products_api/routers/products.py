from typing import Optional
from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, exists

from products_api.core.database import get_session
from products_api.models.products import Product
from products_api.schemas.products import (ProductSchema, ProductPublicSchema, ProductListPublicSchema, ProductUpdateSchema)

router = APIRouter()

@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    response_model=ProductPublicSchema,
    summary='Criar novo produto',
)

async def create_product(product: ProductSchema, db: AsyncSession = Depends(get_session),):
    name_exists = await db.scalar(select(exists().where(Product.name == product.name)))
    if name_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nome do produto já existe",
        )
    
    db_product = Product(
        name=product.name,
        price=product.price,
        description=product.description
    )

    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)

    return db_product

@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=ProductListPublicSchema,
    summary="Listar produtos",
)

async def list_prodcuts(
    db: AsyncSession = Depends(get_session)
):
    
    result = await db.scalars(select(Product))
    products = result.all()

    return {
        'products': products,
    }

@router.get(
    path="/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductPublicSchema,
    summary="Buscar produto por ID",
)

async def get_product(
    product_id: int,
    db: AsyncSession = Depends(get_session),
):
    product = await db.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )
    
    return product

@router.put(
    path="/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductPublicSchema,
    summary="Atualizar produto"
)
async def update_product(
    product_id: int,
    product_update: ProductUpdateSchema,
    db: AsyncSession = Depends(get_session),
):
    product = await db.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )

    update_data = product_update.model_dump(exclude_unset=True)

    if 'name' in update_data and update_data['name'] != product.name:
        name_exists = await db.scalar(
            select(exists().where(
                (Product.name == update_data['name']) &
                (Product.id != product_id)
            ))
        )
        if name_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Nome do produto já existe',
            )

    for field, value in update_data.items():
        setattr(product, field, value)

    await db.commit()
    await db.refresh(product)

    return product

@router.delete(
    path="/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletar o produto",
)
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_session),
):
    product = await db.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )
    
    await db.delete(product)
    await db.commit()

    return
