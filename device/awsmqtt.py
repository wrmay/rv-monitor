import awscrt.mqtt5
import awsiot.mqtt5_client_builder
import time

from awscrt.mqtt5 import PublishPacket

MQTT_ENDPOINT = 'a17sav9lrv8l6k-ats.iot.us-east-2.amazonaws.com'


def on_lifecycle_connection_success(lifecycle_connect_success_data: awsiot.mqtt5.LifecycleConnectSuccessData):
    print(f"Lifecycle Connection Success: {lifecycle_connect_success_data}")
    pub_future = client.publish(PublishPacket(
        topic='rvstate',
        payload=f'Hello at {time.time()}',
        qos=awscrt.mqtt5.QoS.AT_MOST_ONCE))
    pub_future.add_done_callback(lambda x: print(f'publish result: {x.result()}'))


# Callback for the lifecycle event Connection Failure
def on_lifecycle_connection_failure(lifecycle_connection_failure: awsiot.mqtt5.LifecycleConnectFailureData):
    print("Lifecycle Connection Failure")
    print(lifecycle_connection_failure)


if __name__ == '__main__':
    client = awsiot.mqtt5_client_builder.mtls_from_path(
        endpoint=MQTT_ENDPOINT,
        cert_filepath='secrets/test.pem.crt',
        pri_key_filepath='secrets/test-private.pem.key',
        on_lifecycle_connection_success=on_lifecycle_connection_success,
        on_lifecycle_connection_failure=on_lifecycle_connection_failure,
        client_id='fred'
    )
    connect_future = client.start()
    time.sleep(5)
    print('Ciao!')
