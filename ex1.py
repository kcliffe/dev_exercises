def lambda_handler(event, context):
    # initialise configuration params amd logging here
    # ...          
    cfg = { "conn_string": "xyz", "datadog_api_eky": "12345" }      
    conn_string = cfg["conn_string"]
   
    # There may be many physical records
    for record in event['Records']:
   
        # Deserialize the json message
        payload = json.loads(record["body"])

        # A single physical message contains multiple logical messages
        for device_request in payload:
            # extract the primary key
            client_id = device_request['deviceId']
            # and the identifier which denotes the job type
            request_type = device_request['jobType'].lower()
            
            if request_type == 'firmware':
                # publish the firmware message in the payload to the device
                topic = f"job/{client_id}/firmware"
                send(json.dumps(device_request), topic, cfg)
            elif request_type == 'configuration':
                config = compile_configuration(client_id, device_request, conn_string)
                topic = f"job/{client_id}/config"
                send(config, topic, cfg)
   
               
def compile_configuration(client_id, device_request, conn_string):
    # return configuration
    print(f'creating device {client_id} config')
    conn = psycopg2.connect(conn_string)
    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:

        # ...

            cfg = {}
            return cfg
   
 
def send(payload, topic, cfg):
    iot_client=boto3.client('iot-data', endpoint_url=cfg["iotEndpoint"])
    iot_client.publish(topic=topic, payload=json.dumps(config))