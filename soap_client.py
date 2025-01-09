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
            # Step 1: Get the service binding
            # Convert odict_values to list first, then get the first service
            services = list(self.client.wsdl.services.values())
            if not services:
                raise ValueError("No services found in WSDL")
            service = services[0]
            
            # Step 2: Get the first port
            # Convert ports to list first
            ports = list(service.ports.values())
            if not ports:
                raise ValueError("No ports found in service")
            port = ports[0]
            
            # Step 3: Get the operation from the binding
            if operation_name not in port.binding._operations:
                raise ValueError(f"Operation {operation_name} not found in binding")
            operation = port.binding._operations[operation_name]
            
            # Step 4: Get the input message parts
            if not operation.input or not operation.input.body or not operation.input.body.type:
                raise ValueError("Operation input type information not available")
                
            input_parts = {}
            # Some WSDL might have elements differently structured
            if hasattr(operation.input.body.type, 'elements'):
                for name, element in operation.input.body.type.elements:
                    input_parts[name] = str(element.type)
            else:
                # Fallback to getting type directly
                input_parts[operation.input.body.type.name] = str(operation.input.body.type)
            
            return input_parts
            
        except Exception as e:
            raise ValueError(f"Could not get input type for operation {operation_name}: {str(e)}")
