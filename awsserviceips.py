from flask import Flask, render_template

import requests

url = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json")
jurl = url.json()

app = Flask(__name__)


@app.route('/')
def get_service_list():
    """get list of available services, without duplicates"""
    fcn_services = []
    fcn_aws_service_list = []

    for k in jurl['prefixes']:
        fcn_services.append(k['service'])

    for fcn_service in fcn_services:
        if fcn_service in fcn_aws_service_list:
            continue
        else:
            fcn_aws_service_list.append(fcn_service)

    return render_template('list.html', fcn_aws_service_list=fcn_aws_service_list)


if __name__ == '__main__':
    app.run()
