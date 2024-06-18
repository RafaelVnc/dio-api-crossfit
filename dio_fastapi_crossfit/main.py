from fastapi import FastAPI
from dio_fastapi_crossfit.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)
