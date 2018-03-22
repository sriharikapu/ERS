"""
    Function for custom return format
    Supports Error and Success messages

    Parameters
    ----------
    base 
        Base structure for return format
    msg
        Return message or value/s
        Should be JSON format

        Used format is: {'message': value}
        
    Returns
    -------
    dict

"""
def return_msg(base, msg):
    if 'message' in base['result']:
        del base['result']['message']
    elif 'values' in base['result']:
        del base['result']['values']
    else:
        base['result'] = {}
        
    if isinstance(msg, str):
        base['result'].update({'message': msg})
    elif isinstance(msg, list):
        base['result'].update({'values': msg})
    else:
        if (len(base['result'])) > 0:
            base['result'].update(msg)
        else:
            base['result'] = msg
    return base