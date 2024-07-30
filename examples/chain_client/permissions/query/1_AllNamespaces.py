import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    namespaces = await client.fetch_all_permissions_namespaces()
    print(namespaces)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
