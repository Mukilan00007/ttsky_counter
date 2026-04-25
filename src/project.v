`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    // Internal 8-bit register for the counter
    reg [7:0] count;

    // Use ui_in[0] for up/down control
    wire up_down = ui_in[0];

    // Counter Logic
    // Tiny Tapeout uses active-low reset (rst_n)
    always @(posedge clk) begin
        if (!rst_n)
            count <= 8'b00000000;
        else if (up_down)
            count <= count + 1;
        else
            count <= count - 1;
    end

    // Assign internal count to the hardware output pins
    assign uo_out = count;

    // Tie off unused bidirectional pins
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Tie off unused inputs to avoid warnings
    wire _unused = &{ui_in[7:1], uio_in, ena, 1'b0};

endmodule
