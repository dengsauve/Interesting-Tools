############################################################
#
#  Name:         Dennis Sauve
#  Date:         04/30/2017
#  Objective:    Spokane Car Lot Compiler
#  File:         cars.rb
#  Description:  This project is aimed at being able to
#                compile a central list of all cars
#                available in the Greater Spokane Area.
#                The focus ofclass is collecting the data.
#                Formatting and sorting will be handled by
#                another class.
#
############################################################

class Car
  attr_reader :make_model, :price, :url
  def initialize(make_model, price, url)
    @make_model = make_model
    @price = price
    @url = url
  end

  def to_s
    @make_model.ljust(30, '.') + '$' + @price.rjust(11, '.') + ' > ' + @url + "\n"
  end
end