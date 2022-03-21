import ESLogger as eslogger


def lambda_handler(event, context):
    eslogger.info("Event :-")
    eslogger.info(event)
    # params = event['params']
    iteration_max_count = event['iteration_max_count']

    iteration_count = 0
    if 'iteration_count' in event:
        iteration_count = int(event['iteration_count'])
    iteration_count = iteration_count + 1

    result = {
        'iteration_count': iteration_count,
        'iteration_max_count': iteration_max_count,
    }

    return result
