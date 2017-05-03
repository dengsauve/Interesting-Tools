############################################################
#
#  Name:         Dennis Sauve
#  Date:         04/30/2017
#  Objective:    Controlling car_reader.rb
#  File:         main.rb
#  Description:  This is a control for car_reader.rb
#                development is still underway.
#
############################################################
require_relative('car_readers')
require 'ruby-progressbar'

def grand_list
  union_gospel + jennifer_auto + auto_credit_sales + tk_auto + independent + fresh_start + labrosse
end

def union_gospel
  puts 'Retrieving UGM Motors Data'
  ugm = UGMmotors.new('http://www.ugmmotors.org/inventory')
  ugm.car_list
end

def jennifer_auto
  puts 'Retrieving Jennifers Used Cars Data'
  jazz = Jennifers.new('http://www.jennifersautosales.com/content/inventory.php')
  jazz.car_list
end
# Auto Credit Sales  http://www.autocreditsales.com/used-cars-spokane-valley-wa?

def auto_credit_sales
  puts 'Retrieving Auto Credit Sales Data'
  ret_str = ''
  progressbar = ProgressBar.create(:format => '%t [ %B ]')
  (1..30).to_a.each do |page|
    3.times {progressbar.increment}
    acl = AutoCredit.new("http://www.autocreditsales.com/used-cars-spokane-valley-wa?page=#{page}")
    ret_str += acl.car_list
  end
  puts
  ret_str
end

def tk_auto
  puts 'Retrieving TK Auto Sales Data'
  ret_str = ''
  progressbar = ProgressBar.create
  (1..15).to_a.each do |page|
    6.times{progressbar.increment}
    tka = TkAutoSales.new("http://www.tkautosalesspokane.com/used-cars-for-sale-spokane?page=#{page}")
    ret_str += tka.car_list
  end
  puts
  ret_str
end

def independent
  puts 'Retrieving Independent Auto Sales Data'
  ias = IndependentAuto.new('http://www.independentautowa.com/inventory.aspx?cursort=asc&pagesize=500&ordby=price')
  ias.car_list
end

def fresh_start
  puts 'Retrieving Fresh Start Auto Sales Data'
  fsas = IndependentAuto.new('http://www.freshstartas.com/inventory.aspx?cursort=asc&pagesize=500&ordby=price')
  fsas.car_list
end

def labrosse
  puts 'Retrieving Labrosse Auto Sales Data'
  las = TkAutoSales.new('http://www.labrosseautosales.com/used-cars-for-sale-spokane-wa')
  las.car_list
end

puts grand_list


# end of main
