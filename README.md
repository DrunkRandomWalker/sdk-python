## Injective Python SDK

### Dependences

**Ubuntu**
```bash
sudo apt install python3.X-dev
```
**Fedora**
```bash
sudo dnf install python3-devel
```
### Quick Start
```bash
pip install injective-py
```
```python
import injective.chain_client
import injective.exchange_api
```

### Usage
Requires Python 3.7+

[Examples](https://github.com/InjectiveLabs/sdk-python/tree/master/examples)
```bash
$ pipenv shell
$ pipenv install

# connecting to Injective Exchange API
# and listening for new orders from one specific spot market
$ python examples/exchange_api_examples/spot_exchange_rpc/8_StreamOrdersRequest.py

# sending a msg with bank transfer
# signs and posts a Tx to the Injective Chain
$ python examples/chain_client_examples/1_CosmosBankMsgSend.py
```
Upgrade `pip` to the latest version, if you see these warnings:
```
WARNING: Value for scheme.platlib does not match. Please report this to <https://github.com/pypa/pip/issues/10151>    
WARNING: Additional context:   user = True   home = None   root = None   prefix = None
```

### Development

To copy proto schemas and regenerate GRPC clients:

```bash
$ pipenv shell
$ pipenv install --dev

$ make copy-proto
$ make gen
```

## License

Apache Software License 2.0
