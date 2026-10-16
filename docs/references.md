# References and source record

Technical sources consulted on 16 October 2026. Manufacturer examples explain component families and do not identify unreadable parts in the prototype. Diagrams and worked calculations were created for this documentation; manufacturer illustrations are not reproduced.

1. Texas Instruments. **SN74LS86A / 7486 family: Quadruple 2-Input Exclusive-OR Gates.** Supports the XOR and conditional-inversion descriptions. https://www.ti.com/product/SN74LS86A
2. Texas Instruments. **SN7405: inverters with open-collector outputs.** Supports the inverter and pull-up requirements. https://www.ti.com/product/SN7405
3. Texas Instruments. **Data Selectors/Multiplexers**, including SN74150 and SN74LS151. Supports selector operation and the 74150 inverted-output note. https://www.ti.com/lit/ds/symlink/sn74ls151.pdf
4. Texas Instruments. **SN7447A: BCD-to-Seven-Segment Decoders/Drivers.** Supports display compatibility and BCD behavior. https://www.ti.com/product/SN7447A
5. Advanced Photonix. **Light Dependent Resistors.** Supports decreasing resistance with increasing illumination. https://www.advancedphotonix.com/our-products/light-dependent-resistor-ldr
6. University of New Brunswick, EE4253. **Error Correction and the Hamming Code.** Background for parity positions and single-error correction. The report's numeric example and bit order are explicitly defined within this repository. https://www.ece.unb.ca/tervo/ee4253/hamming.shtml
7. NVIDIA, CUDA-Q Academic. **Hamming [7,4,3] Visualizer.** Supports syndrome interpretation and two-bit-error ambiguity. Its displayed bit ordering differs from this repository's position ordering. https://nvidia.github.io/cuda-q-academic/interactive_widgets/hamming.html

## Project-specific material

- Builder's supplied description: laser transmitter; LDR receiver; 7486 XOR and 7405 NOT gates; two 16:1 multiplexers; Hamming single-bit correction; BCD-to-seven-segment display.
- Three supplied project photographs, mapped in [photo-analysis.md](photo-analysis.md). These are retained as original visual evidence.
- No original schematic, BOM, firmware, timing trace, bench log or video file was supplied.
