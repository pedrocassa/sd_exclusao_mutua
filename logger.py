from datetime import datetime

def write_log(file_name, text):
    log_file = open(file_name, 'a')
    
    now = datetime.now()
    datetime_string = now.strftime('%d/%m/%Y %H:%M')
                                                    
    log_file.write(datetime_string + " -- " + str(text) + '\n')
    
    log_file.close()