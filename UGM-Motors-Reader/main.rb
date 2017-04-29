require_relative('car_readers')


def union_gospel
  ugm = UGMmotors.new('http://www.ugmmotors.org/inventory')
  puts ugm.car_list
end

def jennifer_auto
# site: Jennifer's Auto
# URL:  http://www.jennifersautosales.com/content/inventory.php

  jazz = Jennifers.new('http://www.jennifersautosales.com/content/inventory.php')
  puts jazz.car_list
end