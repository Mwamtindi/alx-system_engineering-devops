#!/usr/bin/env ruby

rgx = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
puts ARGV[0].scan(rgx).join(",")
