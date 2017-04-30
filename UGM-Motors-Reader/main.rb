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


def grand_list
  union_gospel + jennifer_auto + auto_credit_sales + tk_auto + independent + fresh_start + labrosse
end

def union_gospel
  ugm = UGMmotors.new('http://www.ugmmotors.org/inventory')
  ugm.car_list
end

def jennifer_auto
  jazz = Jennifers.new('http://www.jennifersautosales.com/content/inventory.php')
  jazz.car_list
end
# Auto Credit Sales  http://www.autocreditsales.com/used-cars-spokane-valley-wa?

def auto_credit_sales
  ret_str = ''
  (1..30).to_a.each do |page|
    acl = AutoCredit.new("http://www.autocreditsales.com/used-cars-spokane-valley-wa?page=#{page}")
    ret_str += acl.car_list
  end
  ret_str
end

def tk_auto
  ret_str = ''
  (1..15).to_a.each do |page|
    tka = TkAutoSales.new("http://www.tkautosalesspokane.com/used-cars-for-sale-spokane?page=#{page}")
    ret_str += tka.car_list
  end
  ret_str
end

def independent
  ias = IndependentAuto.new('http://www.independentautowa.com/inventory.aspx?cursort=asc&pagesize=500&ordby=price')
  ias.car_list
end

def fresh_start
  fsas = IndependentAuto.new('http://www.freshstartas.com/inventory.aspx?cursort=asc&pagesize=500&ordby=price')
  fsas.car_list
end

def labrosse
  las = TkAutoSales.new('http://www.labrosseautosales.com/used-cars-for-sale-spokane-wa')
  las.car_list
end

puts grand_list


# end of main
