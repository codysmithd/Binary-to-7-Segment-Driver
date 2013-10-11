Binary to 7 Segment Display Driver
==========================

VHDL code to take a binary input and convert to 7 segment display. Powered by a huge case statement for easy FPGA synthesis. The case is generated with a python script.

Case Generator Script
----------------------------
The [python script](output_case_generator.py) includes an option for how many numbers the driver should support, the VHDL output signal, and where the case statement gets output to. 

To switch where the output goes simply change `output_type` to either 'print' for printing to the console or 'file' for printing to a file (much faster!). If 'file' is selected, set `filename` to your output file name.



-
Copyright (C) 2013 Cody Smith codysmithd@gmail.com. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details: http://www.gnu.org/licenses/.
