import pandas as pd
from extraction import ClimateExtractor


extractor = ClimateExtractor('London')
extractor.ext_data()

def filter_data(data):
    if 'days' in data and len(data['days']) > 0:
        day = data['days'][0]
        conditions_dict = {
            'date': day['datetime'],
            'condition': day['conditions'],
            'description': day['description'],
            'max_temperature': day['tempmax'],
            'min_temperature': day['tempmin']
        }
        return conditions_dict
    else:
        return None

    
def create_df(filtered_data):
    if filtered_data:
        df = pd.DataFrame([filtered_data])
        print(df)
        return df
    else:
        print("Nenhum dado transformado")


filter_ext_data = filter_data(extractor.data)

create_df(filter_ext_data)

