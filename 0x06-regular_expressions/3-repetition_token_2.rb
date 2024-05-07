#!/usr/bin/env ruby

rgx = /hbt+n/
puts ARGV[0].scan(rgx).join
