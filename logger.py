def write_log(file_name, text):
    log_file = open(file_name, 'a')
    
    datetime = datetime.now()
    datetime_string = datetime.strftime('%d/%m/%Y %H:%M')
                                                    
    log_file.write(datetime_string + ":" + str(text) + '\n')
    
    log_file.close()