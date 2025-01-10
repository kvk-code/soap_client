# SOAP Client

A simple and reusable SOAP client wrapper based on the `zeep` library, providing an easy-to-use interface for making SOAP API calls.

## Features

- Simple interface for SOAP service interactions
- Basic authentication support
- Operation discovery
- Input type inspection
- Configurable timeout
- Error handling

## Requirements

- Python 3.x
- zeep >= 4.2.1
- requests >= 2.31.0

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
    password="optional_password",  # Optional
    timeout=30  # Optional, defaults to 30 seconds
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

## Example

The repository includes an example script (`example.py`) that demonstrates how to use the client with a public SOAP service for number conversions:

```python
from soap_client import SoapClient

# Initialize client with public number conversion service
client = SoapClient("https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL")

# Convert number to words
response = client.call_operation('NumberToWords', ubiNum=42)
print(f"42 in words: {response}")

# Convert number to dollars
response = client.call_operation('NumberToDollars', dNum=123.45)
print(f"123.45 in dollars: {response}")
```

## Error Handling

The client includes built-in error handling for common SOAP-related issues:
- WSDL parsing errors
- Authentication failures
- Invalid operation names
- Invalid input parameters
- Network timeouts

## License

This project is open source and available under the MIT License.
