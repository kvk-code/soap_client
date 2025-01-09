from soap_client import SoapClient

def main():
    # Replace with your WSDL URL
    wsdl_url = "YOUR_WSDL_URL"
    
    # Create client instance
    client = SoapClient(wsdl_url)
    
    # Get available operations
    operations = client.get_available_operations()
    print("Available operations:", operations)
    
    # Example: Get input type for first operation
    if operations:
        first_operation = operations[0]
        input_type = client.get_operation_input_type(first_operation)
        print(f"\nInput type for {first_operation}:")
        print(input_type)
        
        # Example: Call the operation
        # Replace kwargs with actual parameters needed for your operation
        # response = client.call_operation(first_operation, param1="value1", param2="value2")
        # print("Response:", response)

if __name__ == "__main__":
    main()
