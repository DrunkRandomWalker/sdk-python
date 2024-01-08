import asyncio
from typing import Any, Dict

from grpc import RpcError

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def order_event_processor(event: Dict[str, Any]):
    print(event)


def stream_error_processor(exception: RpcError):
    print(f"There was an error listening to derivative orders history updates ({exception})")


def stream_closed_processor():
    print("The derivative orders history updates stream has been closed")


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"

    task = asyncio.get_event_loop().create_task(
        client.listen_derivative_orders_history_updates(
            callback=order_event_processor,
            on_end_callback=stream_closed_processor,
            on_status_callback=stream_error_processor,
            market_id=market_id,
        )
    )

    await asyncio.sleep(delay=60)
    task.cancel()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
