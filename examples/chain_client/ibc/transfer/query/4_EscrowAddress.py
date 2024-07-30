import asyncio

from google.protobuf import symbol_database

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    network = Network.testnet()
    client = AsyncClient(network)

    port_id = "transfer"
    channel_id = "channel-126"

    escrow_address = await client.fetch_escrow_address(port_id=port_id, channel_id=channel_id)
    print(escrow_address)


if __name__ == "__main__":
    symbol_db = symbol_database.Default()
    asyncio.get_event_loop().run_until_complete(main())
