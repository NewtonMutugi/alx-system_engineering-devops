#!/usr/bin/env ruby

regex = /School/
string = ARGV[0]

matches = string.scan(regex)

if matches.any?
  puts matches.join("")
else
  puts ""
end
