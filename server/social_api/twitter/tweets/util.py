def get_all_params(params_dict, expansions, tweet_fields, media_fileds, place_fileds, poll_fields, user_fields):
    params = params_dict
    for variable_names in get_all_params.__code__.co_varnames:
        if variable_names == 'params_dict':
            continue
        else:
            variable_values = locals()[variable_names]
            if variable_values:
                params.update({variable_names: variable_values})
    return params
