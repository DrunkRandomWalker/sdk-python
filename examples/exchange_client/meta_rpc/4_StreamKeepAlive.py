import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = AsyncClient(network)

    task1 = asyncio.get_event_loop().create_task(get_markets(client))
    task2 = asyncio.get_event_loop().create_task(keepalive(client, [task1]))

    try:
        await asyncio.gather(
            task1,
            task2,
        )
    except asyncio.CancelledError:
        print("main(): get_markets is cancelled now")


async def get_markets(client):
    stream = await client.stream_spot_markets()
    async for market in stream:
        print(market)


async def keepalive(client, tasks: list):
    stream = await client.stream_keepalive()
    async for announce in stream:
        print("Server announce:", announce)
        async for task in tasks:
            task.cancel()
        print("Cancelled all tasks")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
