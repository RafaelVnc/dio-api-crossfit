run:
	@uvicorn dio_fastapi_crossfit.main:app --reload

create-migrations:
	@alembic revision --autogenerate -m $(d)

run-migrations:
	@alembic upgrade head