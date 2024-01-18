from flask import Flask, request, jsonify
import requests
import json
app = Flask(__name__)
@app.route('/wassitwebhook', methods=['POST'])
def webhook():
    params = request.json

    # Check if the 'action' parameter is present in the request
    if 'action_name' in params:
        action_name = params['action_name']

        # Perform different actions based on the provided action parameter
        if action_name == 'get_cors_count':
            cust_id = params['user_xxx']
            # Call service 1 and get the response
            response = get_cospnd_count(cust_id)['corspnd_no']
            reply = {'body': 'corees_count',
                     'corr_no': response}
            #reply = json.dumps(reply)
            # whook_reponse=  {
            #     'headers': {
            #         'Content-Type': 'application/json',
            #     },
            #     'statusCode': 200,
            #     'body': reply, }
            hook_reponse= {
                'body': {
                    'param_id': 'corees_count',
                    'corr_no': response
                },
                'headers': {
                    'Content-Type': 'application/json'
                },
                'statusCode': 200
            }

        

        elif action_name == 'action2':
            # Call service 2 and get the response
            whook_reponse = call_service2()

        else:
            # Invalid action, return an error response
            whook_reponse = {'error': 'Invalid action'}

    else:
        # 'action' parameter is missing, return an error response
        whook_reponse = {'error': 'Action parameter is missing'}

    return jsonify(whook_reponse)
    #return whook_reponse
    #return json.dumps(whook_reponse)




# Helper function to call get correspondence count
def get_cospnd_count(cust_id):
    url = 'https://function-coreespondence-count.13zubuptt9c7.eu-de.codeengine.appdomain.cloud/'
    params = {'user_xxx': cust_id}  # Replace with the required parameters
    try:
        # Send a GET request to service 1
        response = requests.get(url, params=params)
        response_data = response.json()
        corspnd_no = response_data['corr_no']
        # Return the response
        return {'corspnd_no': corspnd_no}

    except Exception as e:
        # Handle any errors that occur during the request or processing
        return {'error': str(e)}
    return {'message': 'Service 1 response'}

# Helper function to call service 2
def call_service2():
    # Perform necessary operations
    # ...

    # Return the response
    return {'message': 'Service 2 response'}

if __name__ == '__main__':
    app.run(port=8080)
