import csv

#Abre el archivo csv, lo lee y lo convierte en una lista de diccionarios llamada data[]
#csv_path = './data.csv'


def read_csv(csv_path):
  #country_sales = {}

  with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #next(csv_reader)
    header = next(csv_reader)
    data = []
    for column in csv_reader:
      iterable = zip(header, column)
      country_sales = {key: value for key, value in iterable}

      unwanted_keys = ['category', 'parameter', 'mode', 'unit']
      for unwanted_key in unwanted_keys:
        if unwanted_key in country_sales:
          del country_sales[unwanted_key]
      data.append(country_sales)

    return data


def data_filtered(result_powertrain):
  data_filtered = []
  for item in result_powertrain:
    filtered_item = {
        key: value
        for key, value in item.items() if key not in ['region', 'powertrain']
    }
    data_filtered.append(filtered_item)
  return data_filtered

