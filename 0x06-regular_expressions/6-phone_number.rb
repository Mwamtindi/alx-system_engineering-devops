#!/usr/bin/env ruby

rgx = /\A\d{10}\z/
puts ARGV[0].scan(rgx).join
