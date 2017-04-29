def old_method
  contents = open('http://www.ugmmotors.org/inventory').read.split("\n")
  contents.each do |line|
    if line =~ /title="Link To (\d{4}\s\w+\s\w+)\s&#8212;\s(\S+)\s/ and !line.include?('MECHANIC')
      print $1.ljust(30, '.'), $2.rjust(11,'.')
      if line =~ /a\sclass="post-thumb\simg\sfix\salignleft"\shref="(\S+)"/
        puts "\t"+$1
      else
        puts
      end
    end
  end
end