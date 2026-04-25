import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge

@cocotb.test()
async def test_counter(dut):
    dut._log.info("Starting Counter Test")

    # 1. Start the clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # 2. Initial Values
    dut.ena.value = 1
    # Use individual pin assignments if the bus isn't working
    dut.ui_in.value = 0    
    dut.uio_in.value = 0
    dut.rst_n.value = 0    

    # 3. Reset Sequence
    await Timer(20, units="ns")
    dut.rst_n.value = 1
    await RisingEdge(dut.clk) # Sync with clock after reset
    dut._log.info("Reset released")

    # 4. Test Counting UP
    dut._log.info("Testing UP count...")
    dut.ui_in.value = 1    # ui_in[0] = 1 (Up)
    
    # Wait for 5 cycles
    for i in range(5):
        await RisingEdge(dut.clk)
        # int() conversion can fail if value is 'X', so we handle it
        current_val = str(dut.uo_out.value)
        dut._log.info(f"Cycle {i+1} - Up Count: {current_val}")

    assert int(dut.uo_out.value) == 5, f"Expected 5, got {dut.uo_out.value}"

    # 5. Test Counting DOWN
    dut._log.info("Testing DOWN count...")
    dut.ui_in.value = 0    # ui_in[0] = 0 (Down)
    
    # Wait for 3 cycles (5 -> 4 -> 3 -> 2)
    for i in range(3):
        await RisingEdge(dut.clk)
        dut._log.info(f"Down Count: {str(dut.uo_out.value)}")

    assert int(dut.uo_out.value) == 2, f"Expected 2, got {dut.uo_out.value}"

    dut._log.info("All Counter tests passed!")
