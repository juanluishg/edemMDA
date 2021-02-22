import random
import datetime
import json
import paho.mqtt.client as mqtt
import time
import jwt
import ssl
import pub_to_iot_core


def gen_temp():
    return round(random.uniform(20,40),2)

def gen_frec_card():
    return int(random.uniform(50, 200))

def gen_oxigen():
    return int(random.uniform(90, 100))

def gen_lon():
    return round(random.uniform(-0.36,-0.38),3)

def gen_lat():
    return round(random.uniform(39.4,39.5),3)

def gen_alt():
    return int(random.uniform(0,100))

def gen_pres_art():
    return int(random.uniform(0,150))

def gen_vx():
    return round(random.uniform(-5,5),3)

def gen_vy():
    return round(random.uniform(-5,5),3)

def gen_vz():
    return round(random.uniform(-5,5),3)

def gen_edad():
    start_date = datetime.date(1930, 1, 1)
    end_date = datetime.date(2020, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date.isoformat()

def gen_peso():
    return round(random.uniform(3, 100),1)

def gen_estatura():
    return round(random.uniform(15,40),2)

def gen_genero():
    genero = ["Man", "Female"]
    return genero[int(random.uniform(0,2))]


def make_json():
    res = {}
    res["temp"] =  gen_temp()
    res["frec_card"] = gen_frec_card()
    res["o2"] = gen_oxigen()
    res["lon"] = gen_lon()
    res["lat"] = gen_lat()
    res["alt"] = gen_alt()
    res["pres_art"] = gen_pres_art()
    res["vx"] = gen_vx()
    res["vy"] = gen_vy()
    res["vz"] = gen_vz()
    res["birthdate"] = gen_edad()
    res["weight"] = gen_peso()
    res["height"] = gen_estatura()
    res["gender"] = gen_genero()

    jsonRes = json.dumps(res)

    return jsonRes


def on_publish(client,userdata,result):
    print(result)


# [START iot_mqtt_jwt]
def create_jwt(project_id, private_key_file, algorithm):
    """Creates a JWT (https://jwt.io) to establish an MQTT connection.
    Args:
     project_id: The cloud project ID this device belongs to
     private_key_file: A path to a file containing either an RSA256 or
             ES256 private key.
     algorithm: The encryption algorithm to use. Either 'RS256' or 'ES256'
    Returns:
        A JWT generated from the given project_id and private key, which
        expires in 20 minutes. After 20 minutes, your client will be
        disconnected, and a new JWT will have to be generated.
    Raises:
        ValueError: If the private_key_file does not contain a known key.
    """

    token = {
        # The time that the token was issued at
        "iat": datetime.datetime.utcnow(),
        # The time the token expires.
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=20),
        # The audience field should always be set to the GCP project id.
        "aud": project_id,
    }

    # Read the private key file.
    with open(private_key_file, "r") as f:
        private_key = f.read()

    print(
        "Creating JWT using {} from private key file {}".format(
            algorithm, private_key_file
        )
    )

    return jwt.encode(token, private_key, algorithm=algorithm)


# [END iot_mqtt_jwt]



def send_to_mqtt(data):
    broker = "mqtt.googleapis.com"
    port = 8883

    project_id = "dataproject2-303910"

    client = mqtt.Client("projects/"+project_id+"/locations/europe-west1/registries/liip/devices/disp1")
    
    client.username_pw_set(
        username="unused", password=create_jwt(project_id, "private_key.key", "RS256")
    )

    # Enable SSL/TLS support.
    client.tls_set(ca_certs="roots.pem", tls_version=ssl.PROTOCOL_TLSv1_2)

    
    client.on_publish = on_publish
    client.connect(broker, port)
    ret = client.publish("projects/dataproject2-303910/topics/liip", data)
    print(ret)
    client.disconnect()

def main ():
    while True:
        i = 0
        while i < 100:
            print("Iteracion: "+str(i))
            dataJson = make_json()
            pub_to_iot_core.main(dataJson)
            i+=1
        time.sleep(30)


if __name__ == "__main__":
    main()