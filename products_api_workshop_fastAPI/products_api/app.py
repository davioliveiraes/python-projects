from fastapi import FastAPI, status

from products_api.routers import products

app = FastAPI()

app.include_router(
    router=products.router,
    prefix='/api/v1/products',
    tags=['products'],
)


@app.get('/health_check', status_code=status.HTTP_200_OK)
def health_check():
    return {'status': 'ok'}
