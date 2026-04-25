`timescale 1ns / 1ps

module counter_tb;
    // 1. Declare inputs as reg and outputs as wire
    reg clk;
    reg rst;
    reg up_down; // Renamed 'in' to match the module port name
    wire [7:0] count;

    // 2. Instantiate the Unit Under Test (UUT)
    // Using named port mapping is safer than positional mapping
    counter dut (
        .clk(clk),
        .reset(rst),
        .up_down(up_down),
        .count(count)
    );

    // 3. Clock Generation (100MHz / 10ns period)
    always #5 clk = ~clk;

    initial begin
        // 4. Required for waveform viewing in GTKWave
        $dumpfile("counter_tb.vcd");
        $dumpvars(0, counter_tb);

        // 5. Initialize Signals
        clk = 0;
        rst = 1;        // Start in reset
        up_down = 1;    // Default to counting up

        // 6. Release Reset after a full clock cycle
        #15 rst = 0;    
        
        // 7. Test Counting Up
        #100;           // Let it count up for 100ns
        
        // 8. Test Counting Down
        #10 up_down = 0; 
        #100;           // Let it count down for 100ns

        // 9. Final Reset Check
        #10 rst = 1;
        #20 rst = 0;

        #100 $finish;
    end

endmodule
