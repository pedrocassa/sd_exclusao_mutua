message_type_dict = {
    "REQUEST": "1",
    "GRANT": "2",
    "RELEASE": "3",
    "END": "4"
}

inverted_message_type_dict = {v: k for k, v in message_type_dict.items()}

def create_message(sender, receiver, message):
    if(not sender or not receiver or not message or not message in message_type_dict): return ""

    return str(sender) + str(receiver) + message_type_dict[message] + "0000000"

def get_values_from_message(message):
    if len(message) == 0: return "", "", ""
        
    return message[0], message[1], inverted_message_type_dict[message[2]] 