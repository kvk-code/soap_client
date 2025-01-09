# SOAP Client

A simple and reusable SOAP client based on the `zeep` library.

## Installation

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Import the SoapClient class:
```python
from soap_client import SoapClient
```

2. Create a client instance:
```python
client = SoapClient(
    wsdl_url="your_wsdl_url",
    username="optional_username",  # Optional
    password="optional_password"   # Optional
)
```

3. Get available operations:
```python
operations = client.get_available_operations()
print(operations)
```

4. Get input type for an operation:
```python
input_type = client.get_operation_input_type("operation_name")
print(input_type)
```

5. Call an operation:
```python
response = client.call_operation("operation_name", param1="value1", param2="value2")
print(response)
```

See `example.py` for a complete usage example.

## Features

- Easy to use interface for SOAP services
- Support for basic authentication
- Automatic handling of complex types
- Error handling and timeout configuration
- Type hints for better IDE support
