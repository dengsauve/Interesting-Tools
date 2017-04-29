require 'open-uri'

class Carlot

  def initialize(website)
    @contents = open(website).read.split("\n")
  end

end


class Jennifers < Carlot


  def retrieve_cars
    cars, make_model, price, details = [], '', '', ''
    @contents.each do |line|
      if line =~ /<span\sstyle="font-size:131%;\sfont-weight:bold;">(.+)<\/span>/
        make_model = $1
      end
      if line =~ /<td\salign="right"\sstyle="font-size:131%;\scolor:#FF0000;\sfont-style:italic;\sfont-weight:bold">(\S+)<\/td>/
        price = $1
      end
      if line =~ /<p>&nbsp;<\/p><a\shref="(.+)">View\sAll\sInfo...<\/a>/
        details = $1
      end
      if line =~ /Year:<\/span>\s?(\d{4})/
        year = $1
        cars << [year, make_model, price, details]
      end
    end
    cars
  end

  def car_list
    ret_str = ''
    retrieve_cars.each do |car|
      ret_str += car[0].ljust(5) + car[1].ljust(40, '.') + car[2].rjust(11, '.') + "\t" + car[3] + "\n"
    end
    ret_str
  end

end


class UGMmotors < Carlot

  def retrieve_cars
    cars = []
    @contents.each do |line|
      if line =~ /title="Link To (\d{4}\s\w+\s\w+)\s&#8212;\s(\S+)\s/ and !line.include?('MECHANIC')
        make_model = $1
        price = $2
        if line =~ /a\sclass="post-thumb\simg\sfix\salignleft"\shref="(\S+)"/
          details = $1
        else
          details = ''
        end
        cars << [make_model, price, details]
      end
    end
    cars
  end

  def car_list
    ret_str=''
    retrieve_cars.each do |car|
      ret_str += car[0].ljust(30, '.') + car[1].rjust(11, '.') + "\t" + car[2] + "\n"
    end
    ret_str
  end

end

