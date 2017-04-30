require_relative('car_readers')


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








# end of main
