#!/usr/bin/env ruby

rgx = /h.n/
puts ARGV[0].scan(rgx).join
