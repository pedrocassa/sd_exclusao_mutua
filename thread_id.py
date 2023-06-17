FILE_NAME = "threadIds.txt"

def get_new_thread_id():
    log_file = open(FILE_NAME, 'r+')
    
    ids = log_file.readlines()

    max_item = max(int(id) for id in ids) if len(ids) > 0 else 0
    
    new_item = max_item + 1
    
    log_file.write(str(new_item) + '\n')
    
    log_file.close()
    
    return new_item
