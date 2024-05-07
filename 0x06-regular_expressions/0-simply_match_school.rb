#!/usr/bin/env ruby

rgx = /School/
puts ARGV[0].scan(rgx).join
