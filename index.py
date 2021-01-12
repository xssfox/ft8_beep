#!/usr/bin/env python3
# Generate using ft8_lib : https://github.com/kgoba/ft8_lib

message="3140652320652537530266365644000014103140652300564763703632706435672612273140652"

# use https://github.com/louisabraham/beep on macos

base_freq = 1000

tone_spacing = 6.25
keying_rate = 6.25

print("#!/bin/sh")
print("beep ", end='')
for code in message:
    tone = int(code)
    freq = base_freq + (tone * tone_spacing)
    print(f" -n -f {freq} -l {(1/keying_rate)*1000} -d 0 -D 0", end='')
print()
