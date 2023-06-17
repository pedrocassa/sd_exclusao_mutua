message_type_dict = {
    "REQUEST": "1",
    "GRANTED": "2",
    "RELEASE": "3",
    "END": "4"
}

inverted_message_type_dict = {v: k for k, v in message_type_dict.items()}

def create_message(sender, message):
    if(not sender or not message or not message in message_type_dict): return ""

    return str(sender) + message_type_dict[message] + "00000000"

def get_values_from_message(message):
    if len(message) == 0: return "", "", ""
        
    return message[0], inverted_message_type_dict[message[2]] 