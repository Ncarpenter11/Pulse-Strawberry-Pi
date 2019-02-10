# Pulse-Strawberry-Pi
using a raspberry pi and an oximeter, this python program allows users to find their pulse
First, one needs to construct an oximeter/photoplethysmograph using a transimpedance amplifier,
and various other electronic instrumentation techniques. With all that, I probably wouldn't be able
to help much.

What this code does is it smoothes out the graph to cancel out the noise, centers the overall average
value taken from the photoplethysmograph, then it detects when the graph goes from positive to negative
and adds that as one heartbeat, basically a local Max. It marks the timecode into an array, then prints
the users pulse, and a graph.
