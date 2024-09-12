import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles

# Valores esperados de los segmentos para cada dígito
expected_segments = [
    0b0111110,  # U
    0b1110111,  # A
    0b1111100,  # B
    0b0111001,  # C
    0b1000000,  # -
    0b1111001,  # E
    0b0111000,  # L
    0b1111001,  # E
    0b0111001,  # C
    0b0110001,  # T
    0b1010000,  # R
    0b0111111,  # O
    0b1010100,  # N
    0b0110000,  # I
    0b0111001,  # C
    0b1110111   # A
]

@cocotb.test()
async def test_7seg(dut):
    clock = Clock(dut.clk, 1, units="ms")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("reset")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1)
    dut.rst_n.value = 1

    # Verificar todos los segmentos
    dut._log.info("check all segments")
    for i in range(16):
        dut._log.info(f"check segment {i}")
        await ClockCycles(dut.clk, 1000)
        
        # Verificar la salida `uo_out` (que contiene `led_out` del módulo Verilog)
        assert int(dut.uo_out.value) == expected_segments[i], f"Mismatch at digit {i}: expected {bin(expected_segments[i])}, got {bin(int(dut.uo_out.value))}"
        
        # Verificar que el `uio_out` esté incrementando como se espera
        expected_uio_out = i % 256  # Asume que `second_counter[7:0]` se incrementa con `digit`
        assert int(dut.uio_out.value) == expected_uio_out, f"Mismatch at digit {i}: expected {expected_uio_out}, got {int(dut.uio_out.value)}"

    dut._log.info("All segments verified successfully")

