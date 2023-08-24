import asyncio
import logging
from app import handle_shopping_list_request, handle_dishes_list_request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()

    try:
        asyncio.run(handle_shopping_list_request())
        asyncio.run(handle_dishes_list_request())
    except Exception:
        print('Error')

    event_loop.close()
