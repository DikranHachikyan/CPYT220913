
# print(f'name is:{__name__}')

if __name__ == '__main__':
    
    config = {
        'title': 'Text Editor',
        'version':'1.2.3',
        'max_tabs':1000,
        'margins':[5,10,10,5]
    }

    for key in config:

        print(f'{key} => {config[key]}')

        if type(config[key]) is list:
            for value in config[key]:
                print(f'  value={value}')

    print('---')