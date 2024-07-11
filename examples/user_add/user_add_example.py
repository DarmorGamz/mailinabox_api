"""
File: user_add_example.py

Description:
    This script demonstrates how to create a new user with the Mail-in-a-Box API. 
    Mail-in-a-Box (https://mailinabox.email/) is an easy-to-deploy mail server 
    solution that turns a cloud server into a working mail server.

Usage:
    Run this script with the necessary parameters to create a new user in your 
    Mail-in-a-Box instance.

Example:
    python user_add_example.py --email user@example.com --password password123

Dependencies:
    - Python 3.x
    - Requests library (install with `pip install requests`)

Parameters:
    - email (str): The email address for the new user.
    - password (str): The password for the new user.

Notes:
    - Ensure that the Mail-in-a-Box instance is running and accessible.

Author:
    Darren Morrison

Date:
    2024-07-11

"""
import os
import sys
import argparse
from dotenv import load_dotenv

# Ommit this if example is ran from root instead of ./examples/*
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mailinabox_api
from mailinabox_api.error import ApiException

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new Mail-in-a-Box user.')
    parser.add_argument('--email', type=str, required=True,
                        help='The email address for the new user.')
    parser.add_argument('--password', type=str, required=True,
                        help='The password for the new user.')

    args = parser.parse_args()

    MAILINABOX_ADMIN_EMAIL = os.getenv('MAILINABOX_ADMIN_EMAIL')
    MAILINABOX_ADMIN_PASSWORD = os.getenv('MAILINABOX_ADMIN_PASSWORD')
    MAILINABOX_HOST = os.getenv('MAILINABOX_HOST')

    with mailinabox_api.ApiClient(host=MAILINABOX_HOST, username=MAILINABOX_ADMIN_EMAIL,
                                  password=MAILINABOX_ADMIN_PASSWORD) as api_client:
        # Create an instance of the API class
        api_instance = mailinabox_api.UserApi(api_client)

        try:
            # Add DNS custom A record
            api_response = api_instance.add_user(args.email, args.password)
            print(api_response.status_code)
            print(api_response.text)
        except ApiException as e:
            print("Exception when calling UserApi->add_user: %s\n" % e)
