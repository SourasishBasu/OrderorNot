import json
import random

def lambda_handler(event, context):
    random_number = random.randint(1, 3)
    
    # Map the number to a response
    if random_number == 1:
        response = "yes"
    elif random_number == 2:
        response = "no"
    else:
        response = "maybe"
    
    return {
        'statusCode': 200,
        'body': response
    }
