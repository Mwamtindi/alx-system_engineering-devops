#!/usr/bin/env ruby
#Script to find regex that will match given cases
puts ARGV[0].scan(/hbt{2,5}n/).join
