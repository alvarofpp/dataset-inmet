def clean_date(value):
    return value.replace('/', '-')


def clean_hour(value):
    if 'UTF' in value:
        value = '{}:{}'.format(value[0:2], value[3:5])
    return value


def clean_numeric(value):
    value = str(value)
    if value in ['-9999', 'F', 'nan']:
        return 0

    value = value.replace(',', '.')

    if '.' in value:
        return float(value)


    return int(value)
