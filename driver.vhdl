library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity seven_segment_decode is
  port(
  input : in STD_LOGIC_VECTOR(1 to 10);
  clk   : in STD_LOGIC;
  
  hund_output: out STD_LOGIC_VECTOR(1 to 7);
  tens_output: out STD_LOGIC_VECTOR(1 to 7);
  ones_output: out STD_LOGIC_VECTOR(1 to 7)
  );
end seven_segment_decode;

architecture Behavioral of seven_segment_decode is
  signal output_signal : STD_LOGIC_VECTOR(1 to 21);
  begin
  
  output_signal <= --Generated Text Here
  
  hund_output <= output_signal(1 to 7);
  tens_output <= output_signal(8 to 14);
  hund_output <= output_signal(15 to 21);

end Behavioral;
