import uvicorn
from litestar import Litestar, get
from litestar.contrib.prometheus import PrometheusConfig, PrometheusController


@get("/")
async def index() -> str:
    return "Hello, world! litestar"


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


def get_app():
    prometheus_config = PrometheusConfig()
    return Litestar([index, get_book, PrometheusController], middleware=[prometheus_config.middleware])


app = get_app()
