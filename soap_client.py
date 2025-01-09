from typing import Any, Dict, Optional
import zeep
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth

class SoapClient:
    def __init__(
        self,
        wsdl_url: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        timeout: int = 30
    ):
        """
        Initialize SOAP client with WSDL URL and optional authentication.
        
        Args:
            wsdl_url: URL to the WSDL document
            username: Optional username for basic auth
            password: Optional password for basic auth
            timeout: Request timeout in seconds
        """
        self.wsdl_url = wsdl_url
        
        # Set up session with authentication if provided
        session = Session()
        if username and password:
            session.auth = HTTPBasicAuth(username, password)
        
        # Configure transport with session and timeout
        transport = Transport(session=session, timeout=timeout)
        
        try:
            self.client = zeep.Client(wsdl=wsdl_url, transport=transport)
        except Exception as e:
            raise Exception(f"Failed to initialize SOAP client: {str(e)}")
    
    def get_available_operations(self) -> list:
        """Get list of available SOAP operations."""
        return [op for op in self.client.service._operations.keys()]
    
    def call_operation(self, operation_name: str, **kwargs) -> Any:
        """
        Call a SOAP operation with given parameters.
        
        Args:
            operation_name: Name of the SOAP operation to call
            **kwargs: Parameters to pass to the operation
            
        Returns:
            Response from the SOAP service
        """
        try:
            operation = getattr(self.client.service, operation_name)
            response = operation(**kwargs)
            return response
        except Exception as e:
            raise Exception(f"Failed to call operation {operation_name}: {str(e)}")
    
    def get_operation_input_type(self, operation_name: str) -> Dict:
        """
        Get the expected input type for a given operation.
        
        Args:
            operation_name: Name of the SOAP operation
            
        Returns:
            Dictionary describing the expected input parameters
        """
        try:
            operation = self.client.service._operations[operation_name]
            return operation.input.signature()
        except KeyError:
            raise ValueError(f"Operation {operation_name} not found")
