## How it works
This project is an 8-bit synchronous Up/Down counter. 

- **Inputs**: It uses `ui_in[0]` as the control signal. 
  - When `ui_in[0]` is **High (1)**, the counter increments on every clock cycle.
  - When `ui_in[0]` is **Low (0)**, the counter decrements on every clock cycle.
- **Reset**: The design uses an active-low reset (`rst_n`). When low, the counter is cleared to `0`.
- **Output**: The current 8-bit count value is displayed on the `uo_out[7:0]` bus.

## How to test
1. **Reset**: Hold `rst_n` low for at least one clock cycle to initialize the counter to 0.
2. **Count Up**: Set `ui_in[0]` to 1. Provide a clock signal. You will see `uo_out` incrementing (0, 1, 2, 3...).
3. **Count Down**: Set `ui_in[0]` to 0. Provide a clock signal. You will see `uo_out` decrementing (e.g., from 3 back to 2, 1, 0).
4. **Wrap-around**: If the counter reaches 255 while counting up, the next value will be 0. If it is at 0 while counting down, the next value will be 255.

## External hardware
None required. The counter state can be monitored using 8 LEDs connected to the `uo_out` pins.
