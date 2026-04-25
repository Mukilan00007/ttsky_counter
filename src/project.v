`default_nettype none

module counter (
    input  wire clk,
    input  wire reset,    // Active-high reset
    input  wire up_down,  // 1 for Up, 0 for Down
    output reg [7:0] count
);

    // Added 'posedge reset' to make it an Asynchronous Reset
    always @(posedge clk or posedge reset) begin
        if (reset)
            count <= 8'b00000000;
        else if (up_down)
            count <= count + 1;
        else
            count <= count - 1;
    end

endmodule
