#!/usr/bin/env python3

def get_element_pool():
    """
    """
    try: 
        pool_id = projects.fetch_element_pool(element)
    except Exception as error:
        app.logger.exception(error)
        return '', 400

    return pool_id, 200


def register_elements():
    """
    """
    try:
        element_project = projects.fetch(_id)
        projects.register_elements(elements)
    except Exception as error:
        app.logger.exception(error)
        return '', 400

    return '', 200


def create_project():
    """
    """
    try:
        _id = projects.create(
                name=name, elements=elements, 
                num_of_pools=num_of_pools)
        projects.register_elements(elements)
    except Exception as error:
        app.logger.exception(error)

    return _id, 200
