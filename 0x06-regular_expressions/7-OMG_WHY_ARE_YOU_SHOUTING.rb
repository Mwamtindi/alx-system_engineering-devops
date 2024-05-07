#!/usr/bin/env ruby

rgx = /[A-Z]/
puts ARGV[0].scan(rgx).join
