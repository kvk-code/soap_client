from soap_client import SoapClient

def main():
    # Replace with your WSDL URL
    wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
    
    try:
        # Create client instance
        client = SoapClient(wsdl_url)
        
        # Get available operations
        operations = client.get_available_operations()
        print("Available operations:", operations)
        
        # Show input types for both operations
        print("\nOperation Input Types:")
        print("---------------------")
        for operation in operations:
            try:
                input_type = client.get_operation_input_type(operation)
                print(f"\n{operation}:")
                for param, type_info in input_type.items():
                    print(f"  - {param}: {type_info}")
            except ValueError as e:
                print(f"\n{operation}: {str(e)}")
        
        print("\nExample Operations:")
        print("-----------------")
        # Example: Convert number to words
        number = 42
        try:
            response = client.call_operation('NumberToWords', ubiNum=number)
            print(f"\nNumber {number} in words:", response)
        except Exception as e:
            print(f"Error converting number to words: {e}")
        
        # Example: Convert number to dollars
        amount = 123.45
        try:
            response = client.call_operation('NumberToDollars', dNum=amount)
            print(f"\nAmount {amount} in dollars:", response)
        except Exception as e:
            print(f"Error converting to dollars: {e}")
            
    except Exception as e:
        print(f"Error initializing SOAP client: {e}")

if __name__ == "__main__":
    main()
