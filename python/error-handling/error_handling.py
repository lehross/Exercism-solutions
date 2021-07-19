def handle_error_by_throwing_exception():
    raise Exception("Failed while doing something")


def handle_error_by_returning_none(input_data):
    if input_data.isdigit():
        return int(input_data)
    return None


def handle_error_by_returning_tuple(input_data):
    if input_data.isnumeric():
        return (True, int(input_data))
    return (False, input_data)


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.open()
        filelike_object.do_something()
        filelike_object.close()
    except:
        filelike_object.close()
        raise Exception("Failed while doing something")
