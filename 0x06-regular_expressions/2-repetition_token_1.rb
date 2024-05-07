#!/usr/bin/env ruby

rgx = /hb?tn/
puts ARGV[0].scan(rgx).join
