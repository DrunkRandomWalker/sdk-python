import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    denom = "inj"
    namespace = await client.fetch_permissions_namespace_by_denom(denom=denom, include_roles=True)
    print(namespace)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
