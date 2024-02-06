def data_by_country(data, country):
  filtered_data = list(filter(lambda item: item['region'] == country, data))
  return filtered_data


def data_by_powertrain(result_country, powertrain):
  if powertrain == 'PHEV':
    data = list(
        filter(lambda item: item['powertrain'] == 'PHEV', result_country))
  elif powertrain == 'BEV':
    data = list(
        filter(lambda item: item['powertrain'] == 'BEV', result_country))
  return data


def get_chart(result):
  # union of years with values
  year_value_dict = {item['year']: item['value'] for item in result}
  print('-'*20)
  print(year_value_dict)
  result_dict = {
      '2016': int(year_value_dict['2016']),
      '2017': int(year_value_dict['2017']),
      '2018': int(year_value_dict['2018']),
      '2019': int(year_value_dict['2019']),
      '2020': int(year_value_dict['2020']),
      '2021': int(year_value_dict['2021']),
      '2022': int(year_value_dict['2022'])
  }
  labels = list(result_dict.keys())
  values = list(result_dict.values())
  return labels, values
