import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, ClockCycles


segments = [ 62, 119, 124, 57, 64, 121, 56, 121, 57, 49, 80, 63, 84, 48, 57, 119 ]

@cocotb.test()
async def test_7seg(dut):
    dut._log.info("start")
    clock = Clock(dut.clk, 1, units="ms")
    cocotb.start_soon(clock.start())

    # reset
    dut._log.info("reset")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1)
    dut.rst_n.value = 1

    dut._log.info("check all segments")
    # check all segments and roll over
    for i in range(16):
        dut._log.info("check segment {}".format(i))
        await ClockCycles(dut.clk, 1000)
        assert dut.uio_oe == 0xFF
