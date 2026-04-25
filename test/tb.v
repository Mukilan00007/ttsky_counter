module counter_tb;
reg clk;
reg rst;
reg in;
wire[7:0]count;

counter dut(clk,rst,in,count);
always #5 clk=~clk;
initial begin
clk=0;
rst=1;
in=1;
#10 rst=0;

#50 in=1;
#50 in=0;

#500 $finish;
end
endmodule
