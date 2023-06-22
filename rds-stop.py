pcimport boto3

def lambda_handler(event, context):
    # Initialize AWS clients
    rds = boto3.client('rds')

    # Define a list of RDS instance identifiers
    db_instance_identifiers = ['DB-Instance-Name1', 'DB-Instance-Name2', 'DB-Instance-Name3']

    for db_instance_identifier in db_instance_identifiers:
        try:
            # Describe the RDS instance
            response = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
            db_instance = response['DBInstances'][0]

            # Check if the instance status is "available"
            if db_instance['DBInstanceStatus'] == 'available':
                # Stop the RDS instance
                rds.stop_db_instance(DBInstanceIdentifier=db_instance_identifier)
        except Exception as e:
            print(f"Error occurred while processing instance {db_instance_identifier}: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'RDS instances stopped successfully'
    }
