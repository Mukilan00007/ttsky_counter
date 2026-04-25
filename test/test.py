import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge

@cocotb.test()
async def test_counter(dut):
    dut._log.info("Starting Counter Test")

    # 1. Start the clock (10ns period = 100MHz)
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # 2. Initial Values
    dut.ena.value = 1
    dut.ui_in.value = 0    # ui_in[0] is up_down
    dut.uio_in.value = 0
    dut.rst_n.value = 0    # Start in reset (Assuming active-low rst_n)

    # 3. Reset Sequence
    await Timer(20, units="ns")
    dut.rst_n.value = 1
    dut._log.info("Reset released")

    # 4. Test Counting UP
    dut._log.info("Testing UP count...")
    dut.ui_in.value = 1    # Set up_down (ui_in[0]) to 1
    
    # Wait for 5 clock cycles
    for i in range(5):
        await RisingEdge(dut.clk)
        dut._log.info(f"Up Count: {int(dut.uo_out.value)}")

    assert int(dut.uo_out.value) == 5, f"Expected 5, got {int(dut.uo_out.value)}"

    # 5. Test Counting DOWN
    dut._log.info("Testing DOWN count...")
    dut.ui_in.value = 0    # Set up_down (ui_in[0]) to 0
    
    # Wait for 3 clock cycles (5 -> 4 -> 3 -> 2)
    for i in range(3):
        await RisingEdge(dut.clk)
        dut._log.info(f"Down Count: {int(dut.uo_out.value)}")

    assert int(dut.uo_out.value) == 2, f"Expected 2, got {int(dut.uo_out.value)}"

    # 6. Test Reset during operation
    dut.rst_n.value = 0
    await Timer(10, units="ns")
    assert int(dut.uo_out.value) == 0, "Counter did not reset to 0"
    
    dut._log.info("All Counter tests passed!")
    
