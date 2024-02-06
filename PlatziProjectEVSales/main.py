import csv_reader
import utils
import charts


def run():
  # Read the data from the csv file and store it in a variable DATA
  data = csv_reader.read_csv('./data.csv')
  # Makes a dictionary for a selected country
  country = input('Type Country => ')
  result_country = utils.data_by_country(data, country)
  # Makes a dictionary for a selected powertrain
  powertrain = input('Type Powertrain "BEV or PHEV" => ')
  result_powertrain = utils.data_by_powertrain(result_country, powertrain)
  # Makes a dictionary with unwanted keys 'region', 'powertrain'
  result = csv_reader.data_filtered(result_powertrain)

  #Grafica
  labels, values = utils.get_chart(result)
  #charts.generate_bar_chart(labels, values)
  charts.generate_pie_chart(labels, values)
  

run()
